import math 

class Forme():
    def __init__(self) :
        pass
    
    def Aire():
        return 0
    
class Rectangle(Forme) :
    def __init__(self, L, l):
        super().__init__()
        self.L = L
        self.l = l
        
    def Aire(self) :
        return self.L * self.l
    
class Cercle(Forme) :
    def __init__(self, radius):
        self.radius = radius
        
    def Aire(self) :
        a = math.pi * self.radius ** 2
        return a
        
    
rectangle = Rectangle(10, 21)
cercle = Cercle(5)
airerec = rectangle.Aire()
airecercle = cercle.Aire()
print(airerec)
print(airecercle)