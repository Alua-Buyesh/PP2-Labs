def g(N):
    i=N
    while i>=0:
        yield i
        i-=1

N=int(input("I:"))
x=g(N)
for i in x:
    print(i)