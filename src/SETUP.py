import os
import re

USER_ROOT_PATH = "/Users/kazikgarstecki/Desktop/test_dir"
STORING_DESTINATION = "/Users/kazikgarstecki/Desktop/FV_folder/"
REGEX_PATTERN = re.compile(r"^FV_.*(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})\.(pdf|docx)$")

def check_for_valid_paths():
    if not os.path.exists(USER_ROOT_PATH):
        return ValueError("USER_ROOT_PATH is not valid")
    
def check_for_dest():
    if not os.path.isdir(STORING_DESTINATION):
        try:
            os.mkdir(STORING_DESTINATION)
        except:
            raise ValueError("STORING_DESTINATION is invalid")
    