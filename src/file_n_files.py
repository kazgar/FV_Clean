import os 

class File:
    def __init__(self, path, year, month):
        self._path = path
        self._year = year
        self._month = month
        self._name = os.path.split(self._path)[1]
    
    def __repr__(self):
        return f"File({self._path}, {self._year}, {self._month})"

class Files:
    def __init__(self):
        self._files = []
        self._years = []
        self._year_month = {}

    def add_file(self, file):
        if file not in self._files:
            self._files.append(file)
        if file._year not in self._years:
            self._years.append(file._year)

    def files_from_year(self, year):
        fl_year = []
        for file in self._files:
            if file._year == str(year) and file not in fl_year:
                fl_year.append(file)
        return sorted(fl_year, key = lambda x: x._month)
        
