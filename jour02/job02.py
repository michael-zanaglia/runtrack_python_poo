class Livre():
    def __init__(self, titre : str, auteur : str, nb_page : int):
        self.__titre = titre
        self.__auteur = auteur
        if nb_page < 0 :
            nb_page = 0
        self.__nb_page = nb_page
    
    def ModifPage(self, new_t = "", new_a = "", new_page = 0) :
        #Si je ne rentre rien il garde les memes donees
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


livre = Livre("Malevil", "Robert Merle", 0)
livre.Afficher()

livre.ModifPage(new_page=900)
livre.Afficher()