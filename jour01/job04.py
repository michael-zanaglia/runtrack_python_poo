class Personne:
    def __init__(self, prenom : str, name : str) :
        self.name = name
        self.prenom = prenom
        
    def SePresenter(self) :
        print(f"Je suis {self.prenom} {self.name}")
        

personne1 = Personne("Jean", "Dupont") 
personne2 = Personne("Mai", "Ushio") 

personne1.SePresenter()
personne2.SePresenter()
