"""import os

for i in range(0,26):
    b='A'
    a=chr(b+i)+".txt"
    with open(a,"w") as f:
        f.write(f"This is file {a}.")
    with open(a,"r") as f:
        r=f.read()
        print(r)
        """

import os
from string import ascii_uppercase

for i in ascii_uppercase:
    with open(f"{i}.txt", "w") as f:
        f.write(i)
