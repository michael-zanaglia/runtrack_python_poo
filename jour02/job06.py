class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {} 
        self.__statut_commande = "En cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if self.__statut_commande == "En cours":
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "En cours"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print("Impossible d'ajouter un plat, la commande est déjà en cours de traitement.")

    def annuler_commande(self):
        if self.__statut_commande == "En cours":
            self.__plats_commandes.clear()
            self.__statut_commande = "Annulée"
            print("La commande a été annulée.")
        else:
            print("La commande ne peut pas être annulée, elle est déjà terminée ou annulée.")

    def __calculer_total(self):
        total = 0
        for plat in self.__plats_commandes.values():
            total += plat["prix"]
        return total

    def afficher_commande(self):
        print(f"Commande #{self.__numero_commande} - Statut: {self.__statut_commande}")
        for nom_plat, details_plat in self.__plats_commandes.items():
            print(f"{nom_plat}: {details_plat['prix']} € - Statut: {details_plat['statut']}")
        print(f"Total à payer: {self.__calculer_total()} €")

    def calculer_tva(self, taux_tva):
        tva = (self.__calculer_total() * taux_tva) / 100
        return tva



commande1 = Commande(1)
commande1.ajouter_plat("Pizza", 12.5)
commande1.ajouter_plat("Salade", 8.0)
commande1.afficher_commande()
tva_calculée = commande1.calculer_tva(20)
print(f"TVA à payer : {tva_calculée} €")
commande1.annuler_commande()
commande1.afficher_commande()