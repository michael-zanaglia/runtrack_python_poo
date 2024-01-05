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
    def __init__(self, age=15):
        super().__init__(age)
    
    def AllerEnCours(self) :
        print("Je vais en cours.")
        
    def AfficherAge(self) :
        print(f"J'ai {self.age} ans.")
        
        
class Professeur(Personne) :
    def __init__(self, age, matiere) :
        super().__init__(age)
        self.__matiereEnseigne = matiere
        
    def Enseigner(self) :
        print("Le cours va commencer.")

personne = Personne()
eleve = Eleve()
professeur = Professeur(40, "Physique")

eleve.Bonjour()
eleve.AllerEnCours()
eleve.AfficherAge()
professeur.AfficherAge()
professeur.Bonjour()
professeur.Enseigner()
