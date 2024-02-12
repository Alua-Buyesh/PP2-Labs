import math
def area(n,l):
    a=n*l**2
    b=4*math.tan(math.pi/n)
    res=a/b
    return res

n=int(input("Num of sides: "))
l=int(input("Length of side: "))
res=math.floor(area(n,l))
print(res)