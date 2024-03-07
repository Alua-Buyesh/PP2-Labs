import os

def e(way):
    if os.path.exists(way):
        filename = os.path.basename(way)
        directory = os.path.dirname(way)
        print(f"Path '{way}' exists.")
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print("Doesn't exist")

way="/Users/admin/Desktop/codes/pytho/Tsis5/RegEx10.py"
e(way)