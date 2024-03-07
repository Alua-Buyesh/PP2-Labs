import os

def list_directories_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return directories, files

path = "/Users/admin/Desktop/Books"
directories, files = list_directories_files(path)

print("Directories:")
for directory in directories:
    print(directory)

print("\nFiles:")
for file in files:
    print(file)
