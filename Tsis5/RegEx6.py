import re

def rep(t):
    p = r'[ ,.]'
    res = re.sub(p, ':', t)
    return res

text = "kjbh NBHG , HNB, bk.gJHCVNB. bghf "
res = rep(text)
print(res)
