class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y 

    def show(self):
        print(str(self.x)+";"+str(self.y))

    def move(self):
        self.x=int(input("Change x: "))
        self.y=int(input("Change y: "))

    def dist(self):
        c=self.x - self.y
        if c <0:
            c=-c

        return c

    
x=4
y=9
point = Point(x,y)
point.show()
point.move()
print(point.x,point.y)
res=point.dist()
print(res)

