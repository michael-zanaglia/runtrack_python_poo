class Ville() :
    def __init__(self, nom, nb_hab) :
        self.__nom = nom
        self.__nb_hab = nb_hab
        
    def AfficherPopulation(self) :
        if self.__nb_hab == 1000000 or self.__nb_hab == 861635 :
            print(f"Population actuelle : {self.__nb_hab} habitants")
        else :
            print(f"Mis a jour de la population : {self.__nb_hab} habitants")
    
    def get_Nom(self) :
        return self.__nom
    def get_Nb_Hab(self) :
        return self.__nb_hab
    def set_nb_hab(self, new_hab):
        self.__nb_hab = new_hab

class Personne() :
    def __init__(self, nom, age, nom_ville) :
        self.__nom_personne = nom
        self.__age = age
        self.__nom_ville = nom_ville
        
    def AjouterPopulation(self, ville_hab) :
        ville_hab += 1
        return ville_hab
        
    def AfficherInfoPersonne(self):
        print(f"{self.__nom_personne}, {self.__age}, {self.__nom_ville}") 
        
        


ville = Ville("Paris", 1000000)
personne = Personne("John", 45, ville.get_Nom())
ville.AfficherPopulation()
personne.AfficherInfoPersonne()
ville.set_nb_hab(personne.AjouterPopulation(ville.get_Nb_Hab()))
ville.AfficherPopulation()


ville2 = Ville("Marseille", 861635)
personne2 = Personne("Chloé", 18, ville2.get_Nom())
ville2.AfficherPopulation()
personne2.AfficherInfoPersonne()
ville2.set_nb_hab(personne2.AjouterPopulation(ville2.get_Nb_Hab()))
ville2.AfficherPopulation()

personne3 = Personne("Myrtille", 4, ville.get_Nom())
ville.AfficherPopulation()
personne3.AfficherInfoPersonne()
ville.set_nb_hab(personne3.AjouterPopulation(ville.get_Nb_Hab()))
ville.AfficherPopulation()