def g(N):
    for i in range(1,N):
        yield i

N=int(input("I: "))
x=g(N)
for i in x:
    if i%4==0 and i%3==0:
        print(i)