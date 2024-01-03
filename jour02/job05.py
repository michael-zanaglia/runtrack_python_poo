class Voiture() :
    def __init__(self, marque, modele, year, km, en_marche, reservoir) :
        self.__marque = marque
        self.__modele = modele
        self.__year = year
        self.__km = km 
        self.__en_marche = en_marche
        self.__reservoir = reservoir
    
    def setMarque(self, new_marque):
        self.__marque = new_marque
    def get(self):
        return self.__marque
    
    def setModele(self, new_modele):
        self.__modele = new_modele
    def get(self):
        return self.__modele
    
    def setYear(self, new_year):
        self.__year = new_year
    def get(self):
        return self.__year
    
    def setKm(self, new_km):
        self.__km = new_km
    def getKm(self):
        return self.__km
    
    def setReserve(self, new_reserv):
        self.__reservoir = new_reserv
    def getReserve(self):
        return self.__reservoir
        
        
    def Demarrer(self) :
        if self.__VerifierReservoir() :
            if self.__en_marche == False :
                self.__en_marche = True
                print("La voiture peut demarrer.")
            else :
                print("La voiture roule deja.")
        else :
            print("La voiture ne peut pas demarrer.")
    def Arreter(self) :
        if self.__en_marche == True :
            self.__en_marche = False
            
    def __VerifierReservoir(self) :
        if self.__reservoir > 5 :
            return True
        else : 
            return False

voiture = Voiture("Tesla", "Cybertruck", 2023, 10, False, 50)
voiture.Demarrer()
voiture.Demarrer()

voiture.setReserve(5)
voiture.Demarrer()