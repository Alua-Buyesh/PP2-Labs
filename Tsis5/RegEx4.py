import re

def ch(t):
    p ='[A-Z][a-z]+'
    m=re.findall(p,t)
    return m

t="THFg jfG  HGTG  vBvbBnfbvb"
m=ch(t)
print(m)