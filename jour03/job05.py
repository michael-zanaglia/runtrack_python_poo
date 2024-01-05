import random

# Je cree une classe parent pour mes deux personnages
class Personnage():
    def __init__(self, nom, vie, atk, id, crit):
        self.nom = nom
        self.vie = vie
        self.atk = atk
        self.id = id
        self.crit = crit
        self.taux_crit = []
        
    # Je cree une liste de 1 à 100    
    def DefTauxCrit(self) :
        for x in range(1,101) :
            self.taux_crit.append(x)  
            
    def Attaque(self, adversaire):
        # Je verifie si l'id de mes personnages sont different
        if self.id != adversaire.id :
            # dans ma liste defini en amont, je choisis aleatoirement un nombre
            choice = random.choice(self.taux_crit)
            # Si ce nombre est egale ou inferieur a la stat crit alors mon atk est doublé sinon j'attaque normalement.
            if choice <= self.crit :
                adversaire.vie -= self.atk*2
                if adversaire.vie < 0 :
                    adversaire.vie = 0
                print(f" Taux crit! {self.nom} attaque {adversaire.nom} de {self.atk*2} points. Il lui reste {adversaire.vie}.\n")
            else :
                adversaire.vie -= self.atk
                if adversaire.vie < 0 :
                    adversaire.vie = 0
                print(f"{self.nom} attaque {adversaire.nom} de {self.atk} points. Il lui reste {adversaire.vie}.\n")
    # Verification de la vie s'il est à 0 ou non.
    def Verification(self) :
        if self.vie == 0 :
            return False
        else :
            return  True

# Cette classe recuperes les methodes et les attributs de Personnage()
class Joueur(Personnage) :
    # Je defini ma vie en fonction du niveau predefini.
    def PersonnageCreation(self) :
        if game.get_lvl() == 1 :
            self.vie = 30
        elif game.get_lvl() == 2 :
            self.vie = 20
        elif game.get_lvl() == 3 :
            self.vie = 15
            
# Cette classe recuperes les methodes et les attributs de Personnage()
class Bot(Personnage) :
    # Je defini ma vie en fonction du niveau predefini.
    def PersonnageCreation(self) :
        if game.get_lvl() == 1 :
            self.vie = 12
        elif game.get_lvl() == 2 :
            self.vie = 20
        elif game.get_lvl() == 3 :
            self.vie = 25
            
        

# Je defini le niveau de difficulté.
class Jeu():
    def __init__(self):
        self.niveau = 0
        
    def ChoisirNiveau(self) :
        while True :
            try :
                rep = int(input("Quelle niveau de difficulte souhaitez vous ?\n 1. Facile\n 2. Moyen \n 3. Difficile\n"))
            except ValueError :
                print("Rentrez un nombre entier uniquement.")
            if rep == 1 :
                self.niveau = 1
                break
            elif rep == 2 :
                self.niveau = 2
                break
            elif rep == 3 :
                self.niveau = 3
                break
            else :
                print("Veuillez entrez une reponse valide.")
                continue
    
    def get_lvl(self):
        return self.niveau
 
# J'instancie    
game = Jeu()
bot = Bot("Bowser", 10, 4, "#b0b0", 10)
player = Joueur("Mario", 10, 3, "#p0p0", 20)
# Je definis le niveau
game.ChoisirNiveau()


player.PersonnageCreation()
player.DefTauxCrit()

bot.PersonnageCreation()
bot.DefTauxCrit()

# Variable necessaire pour ma condition de victoire
running = True
count_bot = 0
count_player = 0

# Attaque au tour par tour dans une boucle infini. Si victoire je quitte la boucle
while True :
    player.Attaque(bot)
    running = bot.Verification()
    if not running :
        count_player += 1
        break
    bot.Attaque(player)
    running = player.Verification()
    if not running :
        count_bot += 1
        break

if count_player == 1 :
    print("Felicitation vous avez gagnez")
elif count_bot == 1 :
    print("L'ordinateur a gagner")