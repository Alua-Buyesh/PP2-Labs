import os

def l(way):
    directories = []
    files = []
    for i in os.listdir(way):
        full_path = os.path.join(way, i)
        if os.path.isdir(full_path):
            directories.append(i)
        elif os.path.isfile(full_path):
            files.append(i)
    return directories, files

way = "/Users/admin/Desktop/Books"
directories, files = l(way)

print("Directories:")
for directory in directories:
    print(directory)

print("\nFiles:")
for file in files:
    print(file)
