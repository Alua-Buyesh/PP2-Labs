import os

def copy(a, b):
    try:
        with open(a, 'r') as s:
            with open(b, 'w') as d:
                d.write(s.read())
        print(f"'{a}' copied to '{b}' ")
    except FileNotFoundError:
        print(f"File '{a}' not found.")

a = "/Users/admin/Desktop/codes/pytho/Tsis4/Math/math1.py"
b = "copy1.txt"
copy(a, b)
