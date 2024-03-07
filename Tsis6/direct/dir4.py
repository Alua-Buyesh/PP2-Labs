import os

def l(file):
    try:
        with open(file, 'r') as file:
            n = 0
            for line in file:
                n += 1
        return n
    except FileNotFoundError:
        print(f"File '{file}' not found.")
        return -1

file = "/Users/admin/Desktop/codes/pytho/Tsis5/RegEx10.py"
res = l(file)
print(res)
