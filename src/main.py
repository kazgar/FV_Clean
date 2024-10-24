import os
import shutil
import re
from SETUP import *

def main():
    check_for_valid_paths()
    
    if not os.path.isdir(STORING_DESTINATION):
        try:
            os.mkdir(STORING_DESTINATION)
        except:
            raise ValueError("STORING_DESTINATION is invalid")
    
    pattern_matches_to_dest_r(USER_ROOT_PATH, REGEX_PATTERN, STORING_DESTINATION)
    

def pattern_matches_to_dest_r(path, pattern, destination):
    if os.path.isdir(path):
        for file in os.listdir(path):
            pattern_matches_to_dest_r(path=f"{path}/{file}", pattern=pattern, destination=destination)    
    elif os.path.isfile(path):
        if pattern.match(os.path.split(path)[1]):
            shutil.move(path, destination)
    
    

if __name__ == "__main__":
    main()
