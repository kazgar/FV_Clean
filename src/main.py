import os
import shutil
from SETUP import *


def main():
    check_for_valid_paths()
    
    '''
    shutil.move("/Users/kazikgarstecki/Desktop/bilet.pdf", "/Users/kazikgarstecki/Desktop/moje_pliki/")
    '''

    if not os.path.isdir(STORING_LOCATION):
        try:
            os.mkdir(STORING_LOCATION)
        except:
            raise ValueError("STORING_LOCATION is invalid")
    
    

    

if __name__ == "__main__":
    main()
