import os
import shutil
import re
from SETUP import *

def main():
    check_for_valid_paths()
    check_for_dest()
    
    pattern_matches_to_dest_r(USER_ROOT_PATH, REGEX_PATTERN, STORING_DESTINATION)
    dates = create_year_dirs(STORING_DESTINATION)
    create_month_dirs(STORING_DESTINATION, dates)

    

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

def create_year_dirs(path):
    dates = {}
    pattern = re.compile(r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})")
    for file in os.listdir(path):
        date = pattern.findall(file)
        if date:
            year, month = date[0][2], date[0][1]
            if year not in dates:
                dates[year] = [{month: f"{path}{year}"}]
            elif month not in dates[year]:
                dates[year].append({month: f"{path}{year}"})
    for year in dates.keys():
        if not os.path.isdir(f"{path}{year}"):
            os.mkdir(f"{path}{year}")
    return dates

def create_month_dirs(path, dates_dict):
    for year in dates_dict:
        for item in dates_dict[year]:
            for month_path_dict in dates_dict[year][item]:
                for month, file_path in month_path_dict:
                    print(f"month {month}, file_path {file_path}")
        
            
        
            
                
                    
        

    

if __name__ == "__main__":
    main()
