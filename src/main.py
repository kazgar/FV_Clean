import os
import shutil
import re
from SETUP import *
from file_n_files import File, Files

def main():
    check_for_valid_paths()
    check_for_dest()
    
    pattern_matches_to_dest_r(USER_ROOT_PATH, REGEX_PATTERN, STORING_DESTINATION)
    files = convert_files_to_file_class(STORING_DESTINATION)

    

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
                                                                   

if __name__ == "__main__":
    main()
