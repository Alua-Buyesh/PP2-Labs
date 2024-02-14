import re

def ch(t):
    p = r'([A-Z])'
    z = re.sub(p, r'_\1', t).lower()
    return z

t = "awesomeSushkiFromBabushka"
res = ch(t)
print(res)
