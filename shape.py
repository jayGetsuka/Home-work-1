import math
class Shape:
    def __init__(self, name, side):
        self.name = name
        self.side = side
        self.area = 0
        self.cir = 0
    def setArea(self):
        pass
    def getcircumference(self):
        pass
    def view(self):
        print("Name: ",self.name, self.area, self.cir)
class Triangle(Shape):
    def __init__(self, len):
        Shape.__init__(self, "Triangle", 3)
        self.len = len
    def setArea(self): #Override Method
        self.area = 0.5 * self.len * self.len
    def getcircumference(self):
        self.cir = self.len * 3
class Circle(Shape):
    def __init__(self, r):
        Shape.__init__(self, "Circle", 0)
        self.r = r
    def setArea(self): #Override Method
        self.area = "{:.2f}".format(math.pi * math.pow(self.r, 2))
    def getcircumference(self):
        self.cir = "{:.2f}".format(2 * math.pi * self.r)

obj = Triangle(8)
obj.setArea()
obj.getcircumference()
obj.view()

obj2 = Circle(10)
obj2.setArea()
obj2.getcircumference()
obj2.view()
