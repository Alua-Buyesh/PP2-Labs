import re
def ch(a,b):
    return bool(re.fullmatch(a,b))

a=r"abb|abbb"
test=["abbbbbbb", "abb","hbnmvjb","abbb"]
for i in test:
    if ch(a,i):
        print("match")
    else:
        print("not match")