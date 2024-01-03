class Rectangle:
    def __init__(self, longeur, largeur) :
        self.__longeur = longeur
        self.__largeur  = largeur
    
    #Assesseur
    def get_long_and_lag(self):
        return self.__longeur, self.__largeur
    
    #Mutateurs 
    def set_long(self, new_L):
        self.__longeur = new_L
    def set_larg(self, new_l):
        self.__largeur = new_l
        
    def AfficherRectangle(self) :
        coordonate = (self.__longeur, self.__largeur)
        print(coordonate)
        z = self.__largeur -1
        for i in range(self.__largeur) :
            if i == 0 or i == z :
                print("|"+("-"*self.__longeur)+"|")
            else :
                print("|"+" "*self.__longeur+"|")


rectangle = Rectangle(10, 5)
print(f"Longeur et largeur : {rectangle.get_long_and_lag()}")
rectangle.AfficherRectangle()

#Modification
rectangle.set_long(20)
rectangle.set_larg(10)
print(f"Longeur et largeur : {rectangle.get_long_and_lag()}")
rectangle.AfficherRectangle()
    