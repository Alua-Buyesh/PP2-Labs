def g(N):
    for i in range(1, N):
        yield i*2
    
N=int(input("I: "))
x=g(N)
for i in x:
    if i<N:
        print(i)
