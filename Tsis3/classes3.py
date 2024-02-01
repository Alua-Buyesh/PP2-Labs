class Rectengle():
    def __init__(self):
        self.leng=int(input("L: "))
        self.width=int(input("W: "))

class Shape(Rectengle):
    def __init__(self):
        super().__init__()
    
    def arr(self):
        self.area= self.leng * self.width
        return self.area
    
ar=Shape()
res=ar.arr()
print("Output: ", res)
