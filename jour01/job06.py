class Animal():
    def __init__(self, age : int = 0, name : str = ""):
        self.age = age
        if name == "" :
            name = self.Nommer()
        self.name = name 
    
    def Viellir(self) :
        print("L'animal a vielli.")
        self.age += 1
    
    def AfficherAge(self) :
        print(f"L'age de l'animal est {self.age}")
    
    def Nommer(self) :
        n = input("Nom de votre animal ?\n")
        return n 
    def AfficherNom(self) :
        print(f"Votre animal s'appelle : {self.name}.")
        

animal = Animal()

animal.AfficherNom()
animal.AfficherAge()
animal.Viellir()
animal.AfficherAge()
