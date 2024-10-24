import os

USER_ROOT_PATH = "/Users/kazikgarstecki/"
STORING_LOCATION = "/Users/kazikgarstecki/Desktop/FV_folder"

def check_for_valid_paths():
    if not os.path.exists(USER_ROOT_PATH):
        return ValueError("USER_ROOT_PATH is not valid")

    