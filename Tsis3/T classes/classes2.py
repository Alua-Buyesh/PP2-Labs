class Shape():
    def g(self):
        print("Input:")
        self.input_val = int(input())

class Square(Shape):
    def __init__(self):
        super().__init__()
        self.leng = None

    def area(self):
        return self.leng ** 2
    

    def g(self):
        super().g()
        self.leng = self.input_val


ar = Square()
ar.g()
res = ar.area()
print("Area:", res)
