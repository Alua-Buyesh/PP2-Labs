import re

def ch(t):
    p = r'([A-Z][^A-Z]*)'
    res = ' '.join(re.findall(p, t))
    return res


t = "TodayIsTheGreatDay!"
res = ch(t)
print(res)
