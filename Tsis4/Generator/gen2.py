def g(N):
    for i in range(1, N//2):
        yield i*2
    
N=int(input("I: "))
x=g(N)
for i in x:
    print(i)
