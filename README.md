# RegEx_Disc_CleanUp
RegEx Disc CleanUp is a python scrip that can be used for looking for files that match a regex pattern, sorting them in a directory based on the date, and creating a backup of those files in respective directories on your google drive. I'm using this script to take care of my Invoice, but it can be really used for anything that you can think of. 

## How it works
It looks for the files that match a specific RegEx pattern. Collects them and checks for dates inside the name of the files. It creates root_folder>year>month>files_from_that_month structure on your disc as well as on your google drive so that you have a backup of your important files.

## Installation
Use the package manager pip/pipx to install necessary packages.
```bash
pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
```

## Setup global variables
```python
# path to the destination in which you want the script to look for the files
USER_ROOT_PATH = "/path/to/destination/to/look"

# path to the destination in which you want to keep the files that match the regex pattern (remember about the backslash at the end)
STORING_DESTINATION = "path/to/storing/destination/name_of_the_folder_to_store_files_in"

# regex pattern that you would like to match
REGEX_PATTERN = re.compile("<regex pattern>")

# name of the root folder for your google drive
DRIVE_ROOT_FOLDER_NAME = "name"
```

## Setup google drive oauth
You need to download a json file from google cloud console with your oauth api key. Put the file in the project directory and rename it to "client_credentials.json". When using the app for the first time, you will be redirected to authorize the app to make changes on your google drive. Once you authorize it, you are all set.

## Adjusting
On a side note, if you want to tailor this app for your own needs, make sure to change the names of the files that you upload and folders that you create. They are set to work with "FV_name_of_the_file_dd-mm-yyyy.pdf" or "FV_name_of_the_file_dd-mm-yyyy.docx". In order to make the app work correctly, for different use case - change the RegEx pattern and tailor functions in main.py.

