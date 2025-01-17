import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import pickle

SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate_user():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "./client_credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return creds

credentials = authenticate_user()
drive_service = build("drive", "v3", credentials=credentials)

def create_drive_folder(folder_name, parent_folder_id=None):
    folder_metadata = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder",
        'parents': [parent_folder_id] if parent_folder_id else []
    }
    created_folder = drive_service.files().create(
        body=folder_metadata,
        fields="id",
    ).execute()
    print(f"Created Folder ID: {created_folder['id']}")
    return created_folder["id"]

def get_drive_folder_id(folder_name, parent_folder_id=None, delete=False):
    results = drive_service.files().list(
        q=f"'{parent_folder_id}' in parents and trashed=false" if parent_folder_id else None,
        pageSize=1000,
        fields="nextPageToken, files(id, name, mimeType)"
    ).execute()
    items = results.get("files", [])
    folder = list(filter(lambda x: x["name"] == folder_name, items))
    return folder[0]["id"]

def drive_folder_exists(folder_name, parent_folder_id=None, delete=False):
    results = drive_service.files().list(
        q=f"'{parent_folder_id}' in parents and trashed=false" if parent_folder_id else None,
        pageSize=1000,
        fields="nextPageToken, files(id, name, mimeType)"
    ).execute()
    items = results.get('files', [])
    is_folder = list(filter(lambda x: x["name"] == folder_name, items))
    if is_folder:
        return True
    return False

def upload_file_2_drive(filepath, parent_folder_id=None):
    filename = os.path.basename(filepath)
    file_metadata = {
        "name": filename,
        "parents": [parent_folder_id] if parent_folder_id else []
    }
    media = MediaFileUpload(filepath, resumable=True)
    uploaded_file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()
    print(f"Uploaded file {uploaded_file["id"]}")
    return uploaded_file["id"]


