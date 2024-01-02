class Produit() :
    def __init__(self, nom, prixHT, TVA) :
        self.nom = nom
        self.prixHT = prixHT
        self.tva = TVA
        self.prixttc = self.CalculerPrixTTC()
        
    def CalculerPrixTTC(self) : 
        prixtva = self.prixHT * (self.tva/100)
        prixttc = self.prixHT + prixtva
        return prixttc
    
    def Afficher(self) :
        infos = f"Nom du produit : {self.nom}\nPrix HT : {self.prixHT} euro(s)\nTva : {self.tva} %\nPrix TTC : {self.prixttc} euro(s)"
        return infos
    
    def ModifierNom(self, nouveau_nom) :
        self.nom = nouveau_nom
        
    
    def ModifierPrix(self, new_HT) :
        self.prixHT = new_HT
        self.prixttc = self.CalculerPrixTTC()


################# (( INITIAL )) ####################        
produit1 = Produit("Tarte au pommes",9, 20)
produit2 = Produit("Fraisier",15, 20)
produit3 = Produit("Champagne", 35, 25)
print(produit1.Afficher())
print(produit2.Afficher())
print(produit3.Afficher())


################# (( Modifiés )) ####################      
produit1.ModifierNom("Tarte citron")
produit1.ModifierPrix(5)
print(produit1.Afficher())


produit3.ModifierNom("Vin Blanc")
produit3.ModifierPrix(12)
print(produit3.Afficher())


