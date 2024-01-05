class CompteBancaire() :
    def __init__(self, no, nom, prenom, solde, decouvert) :
        self.__no = no
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
        
    def get_no(self) :
        return self.__no
    def get_sold(self):
        return self.__solde
        
    def AfficherCompte(self) :
        print(f"{self.__prenom} {self.__nom}\n{self.__no}\n{self.__solde}")
    def AfficherSolde(self) :
        print(f"Votre solde est de : {self.__solde} euro(s))")
    def Versement(self, versement) :
        self.__solde += versement
    def Retrait(self, retrait) :
        self.__solde -= retrait
        if self.__solde < 0 and not self.__decouvert :
            print("Retrait impossible")
            self.__solde += retrait
        else :
            agios = (retrait * 20) / 100
            print(f"Vos agios s'élèvent à {agios} euro(s)")
    
    def Virement(self, virement, destinataire):
        if destinataire.get_no() != self.__no :
            self.__solde -= virement
            if self.__solde < 0 and not self.__decouvert :
                print("Virement impossible")
                self.__solde += virement
            else :
                destinataire.Versement(virement)
                print("Virement effectué")
                
        
        

compte = CompteBancaire("Q75FA85D6", "Doe", "John", 5, False)  
compte.AfficherSolde()
compte.Versement(12)
compte.Retrait(0)
# Le compte est a 17 euros
compte.AfficherSolde()

compte2 = CompteBancaire("P86GB96F9", "Dupont", "Jean", 0, True)
compte2.Retrait(11)
# Le compte2 peut avoir le decouvert il est a -11 euros
compte2.AfficherSolde()

# Je fais un virement de 11 euros sur le compte 2 pour retourner a 0
compte.Virement(11, compte2)
compte.AfficherSolde()
compte2.AfficherSolde()