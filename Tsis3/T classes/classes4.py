class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y 

    def show(self):
        print(str(self.x)+";"+str(self.y))

    def move(self):
        global x, y
        x=int(input("Change x: "))
        y=int(input("Change y: "))

    def dist(self):
        self.r=int(input("From x:"))
        self.t=int(input("From y:"))
        c=((self.x-self.r)**2 + (self.y-self.t)**2)**0.5

        return c

    
x=4
y=9
point = Point(x,y)
point.show()
point.move()
print(x,y)
res=point.dist()
print(res)
