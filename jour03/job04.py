class Joueur() :
    def __init__(self, nom, numero, position, buts, passes, carton_jaune, carton_rouge) :
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes = passes
        self.carton_jaune = carton_jaune
        self.carton_rouge = carton_rouge
        
    def MarquerUnBut(self) :
        self.buts += 1
    def EffectuerUnePasseDecisive(self) :
        self.passes += 1
    def RecevoirUnCartonJaune(self) :
        self.carton_jaune += 1
    def RecevoirUnCartonRouge(self) :
        self.carton_rouge += 1
    def AfficherStatistiques(self, team) :
        print(f"\nInfos Joueur :\nNom : {self.nom}\nEquipe : {team}\nNumero : {self.numero}\nPosition : {self.position}\nBut(s) : {self.buts}\nPasse(s) Décisive(s) : {self.passes}\nCarton(s) Jaune(s): {self.carton_jaune}\nCarton Rouge : {self.carton_rouge}\n")
        
        
class Equipe():
    def __init__(self, equipe) :
        self.equipe = equipe
        self.liste = []
    
    def AjouterJoueur(self, player) :
        self.liste.append(player)
    
    def AfficherStatistiqueJoueurs(self) :
        for players in self.liste :
            players.AfficherStatistiques(self.equipe)

joueur1 = Joueur("Messi", 10, "Attaque", 3, 5, 1, 0)
joueur2 = Joueur("Benzema", 8, "Milieu", 2, 0, 2, 0)
joueur3 = Joueur("Mbappé", 8, "Attaque", 7, 2, 0, 1)
team1 = Equipe("Barcelona")
team2 = Equipe("Paris")
team1.AjouterJoueur(joueur1)
team1.AjouterJoueur(joueur2)
team2.AjouterJoueur(joueur3)
team1.AfficherStatistiqueJoueurs()
team2.AfficherStatistiqueJoueurs()

joueur2.MarquerUnBut()
joueur3.MarquerUnBut()
joueur2.MarquerUnBut()
joueur3.MarquerUnBut()
joueur3.MarquerUnBut()
joueur1.EffectuerUnePasseDecisive()
team1.AfficherStatistiqueJoueurs()
team2.AfficherStatistiqueJoueurs()