import os

def o(way):
    if os.path.exists(way):
        if os.path.isfile(way):
            print("File exists")
            return True
        else:
            print("Path is a directory, not a file")
            return False
    else:
        print("File not found")
        return False
def r(way):
    if o(way):
        f=open(way,"r")
        print(f.read())
        f.close()

way = "/Users/admin/Desktop/codes/pytho/Tsis5/RegEx1.py"
r(way)
