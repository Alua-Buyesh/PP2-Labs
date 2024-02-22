import re

def ch(t):
    p='_(.)'
    rep= lambda m: m.group(1).upper()
    res = re.sub(p, rep, t)
    return res

text="jytfg_gvbn_jhvbnmbm_gvvcd"
res=ch(text)
print(res)