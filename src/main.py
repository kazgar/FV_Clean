import os
import shutil
import re
from SETUP import *
from google_drive import *
from file_n_files import File, Files

def main():
    check_for_valid_paths()
    check_for_dest()
    
    pattern_matches_to_dest_r(USER_ROOT_PATH, REGEX_PATTERN, STORING_DESTINATION)
    files = convert_files_to_file_class(STORING_DESTINATION)
    create_directories(STORING_DESTINATION, files)
    create_google_directories(files)


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
            file._path = path+year+f"/{month}-{year}/"+os.path.basename(file._path)


def create_google_directories(files):
    if not drive_folder_exists(DRIVE_ROOT_FOLDER_NAME):
        id_root_folder = create_drive_folder(DRIVE_ROOT_FOLDER_NAME)
    else:
        id_root_folder =  get_drive_folder_id(DRIVE_ROOT_FOLDER_NAME)
    for year in sorted(files._years, reverse=True):
        files_from_year = files.files_from_year(year)
        if not drive_folder_exists(f"FV_{year}", id_root_folder):
            year_folder_id = create_drive_folder(f"FV_{year}", id_root_folder)
        else:
            year_folder_id = get_drive_folder_id(f"FV_{year}", id_root_folder)
        for file in files_from_year:
            month = file._month
            if not drive_folder_exists(f"{month}-{year}", year_folder_id):
                month_folder_id = create_drive_folder(f"{month}-{year}", year_folder_id)
            else:
                month_folder_id = get_drive_folder_id(f"{month}-{year}", year_folder_id)
            if not drive_folder_exists(os.path.basename(file._path), month_folder_id):
                upload_file_2_drive(file._path, month_folder_id)  
            

if __name__ == "__main__":
    main()
