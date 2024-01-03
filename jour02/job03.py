class Livre():
    def __init__(self, titre : str, auteur : str, nb_page : int, dispo = True):
        self.__titre = titre
        self.__auteur = auteur
        if nb_page < 0 :
            nb_page = 0
        self.__nb_page = nb_page
        self.__dispo = dispo
    
    def ModifPage(self, new_t = "", new_a = "", new_page = 0) :
        #Si je ne rentre rien il garde les memes donnees
        if new_t == "" :
            new_t = self.__titre
        self.__titre = new_t
        if new_a == "" :
            new_a = self.__auteur
        self.__auteur = new_a
        if new_page > 0 :
            self.__nb_page = new_page
        else :
            print("Erreur, veuillez entre un nombre entier positif.")
    
    def Afficher(self) :
        print(f"{self.__titre}, {self.__auteur}, {self.__nb_page} pages.")
    
    def Verification(self):
        print("Verification en cours...")
        return self.__dispo
    def Emprunter(self) :
        if self.__dispo == True :
            print("Le livre vient d'etre emprunté.")
            self.__dispo = False
        else :
            print(f"Vous ne pouvez pas emprunter le livre {self.__titre}. Il a deja été emprunté.")
    def Rendre(self) :
        if self.__dispo == False :
            print("Livre rendu!")
            self.__dispo = True
        else :
            print(f"Le livre {self.__titre} a deja été rendu.")
        
        
        


livre = Livre("Malevil", "Robert Merle", 0)
livre.Afficher()

livre.ModifPage(new_page=900)
livre.Afficher()

livre.Verification()
livre.Emprunter()
livre.Verification()
livre.Emprunter()
livre.Verification()
livre.Rendre()
livre.Verification()
livre.Rendre()
