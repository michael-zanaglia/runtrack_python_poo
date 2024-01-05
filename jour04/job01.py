class Personne() :
    def __init__(self, age = 14) :
        self.age = age
        
    def AfficherAge(self) :
        print(f"{self.age}")
        
    def set_ModifierAge(self, new) :
        self.age = new
        
    def Bonjour(self) :
        print("Hello")
        
class Eleve(Personne) :
    def AllerEnCours(self) :
        print("Je vais en cours.")
        
    def AfficherAge(self) :
        print(f"J'ai {self.age} ans.")
        
        
class Professeur(Personne) :
    def __init__(self, matiere) :
        self.__matiereEnseigne = matiere
        
    def Enseigner(self) :
        print("Le cours va commencer.")

personne = Personne()
eleve = Eleve()
professeur = Professeur("Physique")

eleve.AfficherAge()