class Personnage() :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def Droite(self) :
        self.x += 1
    def Gauche(self) :
        self.x -= 1
    def Haut(self) :
        self.y += 1
    def Bas(self) :
        self.y -= 1
    def Position(self) :
        print(f"Position : ({self.x},{self.y})")
        
        
personnage = Personnage(0,0)
personnage.Droite()
personnage.Droite()
personnage.Droite()
personnage.Bas()
personnage.Bas()
personnage.Bas()
personnage.Gauche()
personnage.Bas()
personnage.Position()