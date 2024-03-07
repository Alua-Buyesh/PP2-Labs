s = str(input())

def u(x):
    if x.isupper():
        return True
    else:
        return False

up = len(list(filter(u, s)))
lo = len(s) - up
print("Upper:",up)
print("Lower:", lo)
