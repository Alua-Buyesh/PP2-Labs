import os

l = ["Me", "You", "Fucking", "tired"]

with open("Dir5a.txt", "wb") as f:
    for i in l:
        f.write(i.encode() + b"\n")

with open("Dir5a.txt", "r") as f:
    print(f.read())
