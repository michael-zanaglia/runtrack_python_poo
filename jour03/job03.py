class Tache() :
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut
        
    def get_titre(self) :
        return self.titre 
    def set_statut(self, new) :
        self.statut = new    
    def get_stat(self) :
        return self.statut   

class ListedeTaches() :
    def __init__(self, liste):
        self.liste = liste
        
    def AfficherListe(self):
        print("La liste est la suivante :")
        for x in self.liste :
            index = self.liste.index(x) + 1
            e = eval(f"tache{index}.get_stat()")
            print(f"{x}, {e}")
        print("\n")
            
    def AjouterTache(self, new_task):
        self.liste.append(new_task)
    def SupprimerTache(self, task) :
        if task.capitalize() in self.liste :
            self.liste.remove(task)
        else :
            print("il n'existe aucune tache de ce nom.")
    def MarquerCommeFinie(self, task) :
        if task in self.liste :
            index = self.liste.index(task) + 1
            eval(f"tache{index}.set_statut('terminer')")
        else :
            print("La tache n'est pas dans la liste.")
    def FiltrerListe(self) :
        print("Voici les tachers restantes :")
        for x in self.liste :
            index = self.liste.index(x) + 1
            e = eval(f"tache{index}.get_stat()")
            if e == "à faire" :
                print(x)
            print("\n")
            
    
    
    
l = []   

    
tache1 = Tache("Course", "Acheter oeuf, lait, sucre", "à faire")
tache2 = Tache("Lessive", "Laver mon linge", "à faire")
tache3 = Tache("Menage", "Depoussierer mon bureau", "terminer")
tache4 = Tache("Sport", "Aller courrir 1h", "à faire")
tache5 = Tache("Brosser", "Brosser les dents", "à faire")

for i in range(4) :
    l.append(eval(f"tache{i+1}.get_titre()"))

liste = ListedeTaches(l)

# Liste initiale
liste.AfficherListe()
# Liste avec un ajout
liste.AjouterTache("Brosser")
liste.AfficherListe()
# Liste en retirant une tache
liste.SupprimerTache("Menage")
liste.AfficherListe()
# Change un statut
liste.MarquerCommeFinie(("course").capitalize())
# Element non fini uniquement
liste.FiltrerListe()


liste.AfficherListe()