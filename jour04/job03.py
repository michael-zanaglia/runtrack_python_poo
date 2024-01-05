class Rectangle() :
    def __init__(self, L, l):
        self.__L = L
        self.__l = l
    
    def Perimetre(self):
        p = 2 * (self.__L + self.__l)
        print(p)
        
    def set_L(self, new_L) :
        self.__L = new_L
        
    def set_l(self, new_l) :
        self.__l = new_l
        
    def Surface(self) :
        A = self.__L * self.__l
        print(A)
        return A
        
class Parallelepipede(Rectangle) :
    def __init__(self, L, l, h) :
        super().__init__(L, l)
        self.h = h
        
    def Volume(self) :
        a = self.Surface()
        V = a * self.h
        print(V)
    
            
rectangle = Rectangle(20,15)
parallelepipede = Parallelepipede(20, 15, 16)
rectangle.Perimetre()
rectangle.Surface()
parallelepipede.Volume()