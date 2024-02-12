def gen(N):
    for i in range(0, N//2):
        yield i**2
    
N=int(input("I: "))
x=gen(N)
for a in x:
    if a<N:
        print(a)