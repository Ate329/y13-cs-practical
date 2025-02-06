import math

class shape():
    def __init__(self, areaV, perimeter):
        self.areaV = areaV
        self.perimeter = perimeter
        
    def area(self, areaV):
        print("Area:", areaV)
    
class rectange(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        super().area(self.length * self.width)

class circle(shape):
    def __init__(self, r):
        self.r = r
        
    def area(self):
        super().area(math.pi * (self.r ** 2))
    
myCircle = circle(2)
myCircle.area()
