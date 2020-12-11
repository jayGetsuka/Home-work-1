class Shape:
    def __init__(self,name):
        self.name = name
    def Area(self):
        pass
class Triangle(Shape):
    def __init__(self,name,height, weight):
        Shape.__init__(self, name)
        self.height = height
        self.weight = weight
    def Area(self):
        print(self.name)
        area = 0.5 * self.height * self.weight
        return area
class Rectangle(Shape):
    def __init__(self, name, wide, long):
        Shape.__init__(self, name)
        self.wide = wide
        self.long = long
    def Area(self):
        print(self.name)
        area = self.wide * self.long
        return area

print("1. Triangle 2.Rectangle")
choose = int(input("1 or 2:"))
if choose == 1:
    inp = eval(input("input height weight: "))
    triangle = Triangle("Triangle", inp[0], inp[1])
    print(triangle.Area())
elif choose == 2:
    inp = eval(input("input wide long: "))
    rectangle = Rectangle("Rectangle", inp[0], inp[1])
    print(rectangle.Area())


