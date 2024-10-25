import os
import shutil
import re
from SETUP import *
from file_n_files import File, Files
from googleapiclient.discovery import build
from google.oauth2 import service_account

def main():
    check_for_valid_paths()
    check_for_dest()
    
    pattern_matches_to_dest_r(USER_ROOT_PATH, REGEX_PATTERN, STORING_DESTINATION)
    files = convert_files_to_file_class(STORING_DESTINATION)
    create_directories(STORING_DESTINATION, files)
    
    creds = service_account.Credentials.from_service_account_file(
        "/Users/kazikgarstecki/Desktop/workspace/github.com/kazgar/RegEx_Disc_CleanUp/regexdisccleanup-e1eddbacc9ee.json", 
        scopes=['https://www.googleapis.com/auth/drive']
        )
    drive_service = build("drive", "v3", credentials=creds)
    
    folder_metadata = {
        "name": "FV",
    }
    try:
        drive_service.files().create(body=folder_metadata, fields='id').execute()
    except Exception as e:
        raise Exception("Exception occured:", e)


def pattern_matches_to_dest_r(path, pattern, destination):
    if os.path.isdir(path):
        for file in os.listdir(path):
            pattern_matches_to_dest_r(path=f"{path}/{file}", pattern=pattern, destination=destination)    
    elif os.path.isfile(path):
        if pattern.match(os.path.split(path)[1]):
            try:
                shutil.move(path, destination)
            except:
                pass

def convert_files_to_file_class(path):
    files = Files()
    pattern = re.compile(r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})")
    for file in os.listdir(path):
        date = pattern.findall(file)
        if date:
            year, month = date[0][2], date[0][1]
            file = File(path+file, year, month)
            files.add_file(file)
    return files

def create_directories(path, files):
    for year in sorted(files._years, reverse=True):
        files_from_year = files.files_from_year(year)
        if not os.path.isdir(path+year):
            os.mkdir(path+year)
        for file in files_from_year:
            month = file._month
            if not os.path.isdir(path+year+f"/{month}-{year}"):
                os.mkdir(path+year+f"/{month}-{year}")
            shutil.move(file._path, path+year+f"/{month}-{year}")
            

            


        
                                                                   

if __name__ == "__main__":
    main()
