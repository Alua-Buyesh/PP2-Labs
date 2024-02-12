def squares(b):
    for i in range(1, b//2):
        yield i**2


a = int(input("a: "))
b = int(input("b: "))

for i in squares(b):
    if i>a and b>i:
        print(i)
