import math
class Vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def mag(self):
        mag = math.atan2(self.y, self.x)
        return(mag)
    def add(self, u):
        self.x = self.x + u.x
        self.y = self.y + u.y

    def scaleMult(self, z):
        self.x = self.x*z
        self.y = self.y*z
    def dotProd(self, u):
        dotX = self.x*u.x
        dotY = self.y*u.y
        return(dotX, dotY)
    
    def angle(self, u):
           
            dot_product = self.dotProd(u)
            magnitude_self = self.mag()
            magnitude_u = u.mag()

           
            if magnitude_self == 0 or magnitude_u == 0:
                return 0.0

            print(f"dot_product: {dot_product}, type: {type(dot_product)}")
            dot_product = int(dot_product)
            print(f"dot_product: {dot_product}, type: {type(dot_product)}")
            cos_theta = dot_product / (magnitude_self * magnitude_u)
            
           
            return(cos_theta)

Nina = Vector(10,10)
print(Nina.mag())


Ramya = Vector(20,10)
Nina.add(Ramya)
print(Nina.dotProd(Ramya))
print(Nina.angle(Ramya))