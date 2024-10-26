# RegEx_Disc_CleanUp
RegEx Disc CleanUp is a python scrip that can be used for looking for files that match a regex pattern, sorting them in a directory based on the date, and creating a backup of those files in respective directories on your google drive. I'm using this script to take care of my Invoice, but it can be really used for anything that you can think of.

## Installation
Use the package manager pip/pipx to install necessary packages.
```bash
pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
```

## Setup
```python
# path to the destination in which you want the script to look for the files
USER_ROOT_PATH = "/path/to/destination/to/look"

# path to the destination in which you want to keep the files that match the regex pattern (remember about the backslash at the end)
STORING_DESTINATION = "path/to/storing/destination/name_of_the_folder_to_store_files_in"

# regex pattern that you would like to match
REGEX_PATTERN = re.compile("<regex pattern>")

# name of the root folder for your google drive
DRIVE_ROOT_FOLDER_NAME = "name"