class Point() :
    def __init__(self, x, y) :
        self.x = x 
        self.y = y
        self.ChangeX()
        self.ChangeY()
        
    def AfficherLesPoints(self) :
        print(f"Les coordonees sont : ({self.x},{self.y})")
    
    def AfficherX(self) :
        print(self.x)
        
    def ChangeX(self) :
        while True :
            yo = input("Souhaitez-vous changer la valeur de x ? (y/n)").lower()
            if yo == "y" :
                self.x = int(input("Inserer la valeur de x :\n"))
                break
            elif yo == "n" :
                print(f"Tres bien, {self.x} est conservé.")
                break
            else :
                print("Entrez une réponse valide.")
    
    def ChangeY(self) :
        while True :
            yo = input("Souhaitez-vous changer la valeur de y ? (y/n)").lower()
            if yo == "y" :
                self.y = int(input("Inserer la valeur de y :\n"))
                break
            elif yo == "n" :
                print(f"Tres bien, {self.y} est conservé.")
                break
            else :
                print("Entrez une réponse valide.")

    def AfficherY(self) :
        print(self.y)
        
        
point = Point(5,10)
point.AfficherLesPoints()
point.AfficherX()
point.AfficherY()