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
    
    
rectangle = Rectangle(10, 21)
aire = rectangle.Aire()
print(aire)