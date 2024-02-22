import re

def ch(t):
    t=t[1:]
    p = '([A-Z])'
    c=lambda m: " "+m.group(0).lower()
    res = re.sub(p,c, t)
    return res

t = "TodayIsTheGreatDay!"
res = ch(t)
print(t[0]+res)
