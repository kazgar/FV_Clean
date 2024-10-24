import os
import re

USER_ROOT_PATH = "/Users/kazikgarstecki/Desktop/test_dir"
STORING_DESTINATION = "/Users/kazikgarstecki/Desktop/FV_folder"
REGEX_PATTERN = re.compile("FV_01-10-2022.jpg")

def check_for_valid_paths():
    if not os.path.exists(USER_ROOT_PATH):
        return ValueError("USER_ROOT_PATH is not valid")

    