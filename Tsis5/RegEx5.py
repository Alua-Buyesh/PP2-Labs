import re

def ch(t):
    p = 'a[a-z]*b$'
    res = []
    for i in t:
        m = re.findall(p, i)
        res.extend(m)
    return res

t = ["ab", 'aucnrb', ',cjrnfn', 'aknfvhbd','ahgjesfdmbncj']
res = ch(t)
print(res)
