import os
import re

USER_ROOT_PATH = "/path/to/destination/to/look"
STORING_DESTINATION = "path/to/storing/destination/name_of_the_folder_to_store_files_in"
REGEX_PATTERN = re.compile(r"^(FV_|fv_).*(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})\.(pdf|docx)$")
DRIVE_ROOT_FOLDER_NAME = "FV"

def check_for_valid_paths():
    if not os.path.exists(USER_ROOT_PATH):
        return ValueError("USER_ROOT_PATH is not valid")
    
def check_for_dest():
    if not os.path.isdir(STORING_DESTINATION):
        try:
            os.mkdir(STORING_DESTINATION)
        except:
            raise ValueError("STORING_DESTINATION is invalid")
        

    