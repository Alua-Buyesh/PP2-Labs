def area(a,b,h):
    res=(a+b)*h/2
    return res

h=int(input("h: "))
a=int(input("a: "))
b=int(input("b: "))

res=area(a,b,h)
print(res)