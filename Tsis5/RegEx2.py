import re
def ch(a,b):
    return bool(re.search(a,b))

a="ab{2}$|ab{3}$"
test=["abbbbbbb", "abb","hbnmvjb","abbb"]
for i in test:
    if ch(a,i):
        print(f"'{i}' match")
    else:
        print(f"'{i}'not match")