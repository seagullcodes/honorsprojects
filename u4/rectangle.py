import math
class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area = self.base*self.height
        return(area)
    def perm(self):
        perm = (2*self.base)+(2*self.height)
        return(perm)
    def diag(self):
        diag = math.sqrt((self.base*self.base)+(self.height*self.height))
        return(diag)

Nina = Rectangle(10,10)
print(Nina.area())
print(Nina.perm())
print(Nina.diag())