import math

class Cercle() :
    def __init__(self, rayon) :
        self.rayon = rayon
        self.ChangerRayon()
        
    def ChangerRayon(self) :
        while True :
            yn = input("Souhaitez vous changer la valeur du rayon ?(y/n)\n").lower()
            if yn == "y" :
                self.rayon = int(input("Inserer une nouvelle valeur :\n"))
                break
            elif yn == "n" :
                print("La valeur reste inchangé.")
                break
            else :
                print("Entrer invalide")
                
    def Diametre(self) :
        print(f"Diamètre du cercle : {self.rayon * 2}")
    
    def Circonference(self) :
        print(f"Circonférence du cercle : {round((self.rayon*2)*math.pi, 2)}")
        
    def Aire(self) :
        print(f"Aire du cercle : {round((self.rayon*self.rayon)*math.pi, 2)}")
    def AfficherInfos(self) :
        print(f"r : {self.rayon}")
        print(f"D : {self.rayon * 2}")
        print(f"C : {round((self.rayon*2)*math.pi, 2)}")
        print(f"Aire : {round((self.rayon*self.rayon)*math.pi, 2)}")
        
cercle = Cercle(7)
cercle.AfficherInfos()