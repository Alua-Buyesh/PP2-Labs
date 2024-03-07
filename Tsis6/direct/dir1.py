import os

def list_directories_files(way):
    directories = [d for d in os.listdir(way) if os.path.isdir(os.path.join(way, d))]
    files = [f for f in os.listdir(way) if os.path.isfile(os.path.join(way, f))]
    return directories, files

way = "/Users/admin/Desktop/Books"
directories, files = list_directories_files(way)

print("Directories:")
for directory in directories:
    print(directory)

print("\nFiles:")
for file in files:
    print(file)
