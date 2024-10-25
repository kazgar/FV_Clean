class File:
    def __init__(self, path, year, month):
        self._path = path
        self._year = year
        self._month = month
    
    def __repr__(self):
        return f"File({self._path}, {self._year}, {self._month})"

class Files:
    def __init__(self):
        self._files = []
        self._years = []

    def add_file(self, file):
        if file not in self._files:
            self._files.append(file)
        if file._year not in self._years:
            self._years.append(file._year)