import os
import shutil
import re
from SETUP import *

def main():
    check_for_valid_paths()
    check_for_dest()
    
    pattern_matches_to_dest_r(USER_ROOT_PATH, REGEX_PATTERN, STORING_DESTINATION)

    create_directories_month_year(STORING_DESTINATION)

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

def create_directories_month_year(path):
    dates = {}
    pattern = re.compile(r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})")
    for file in os.listdir(path):
        date = pattern.findall(file)
        if date:
            year, month = date[0][2], date[0][1]
            if year not in dates:
                dates[year] = [{month: path+file}]
            elif month not in dates[year]:
                dates[year].append({month: path+file})
    for year in dates.keys():
        os.mkdir(path+year)

                
                    
        

    

if __name__ == "__main__":
    main()
