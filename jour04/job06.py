class Vehicule() :
    def __init__(self, marque, modele, year, prix) :
        self.marque = marque
        self.modele = modele
        self.year = year
        self.prix = prix
        
    def InformationVehicule(self) :
        print(f"Informations :\n Marque = {self.marque}\n Modele = {self.modele}\n Année = {self.year}\n Prix = {self.prix}")
    
    def Demarrer(self) :
        print("Attention je roule.")
    
class Voiture(Vehicule) :
    def __init__(self, marque, modele, year, prix, porte = 4) :
        super().__init__(marque, modele, year, prix)
        self.porte = porte
        
    def InformationVehicule(self) :
        super().InformationVehicule()
        print(f" Nombre de porte : {self.porte}")
        
    def Demarrer(self) :
        print("C'est parti ! En voiture Simone !")

class Moto(Vehicule) :
    def __init__(self, marque, modele, year, prix, roue = 2) :
        super().__init__(marque, modele, year, prix)
        self.roue = roue
        
    def InformationVehicule(self) :
        super().InformationVehicule()
        print(f" Nombre de roue : {self.roue}")
    
    def Demarrer(self) :
        print("Jour de pluie. Faites attention lorsque vous roulerez.")


voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
voiture.InformationVehicule()
moto.InformationVehicule()

voiture.Demarrer()
moto.Demarrer()