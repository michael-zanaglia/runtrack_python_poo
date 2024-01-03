class Student() :
    def __init__(self, nom, prenom, id, credit, level = "") :
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credit = credit
        if level == "" :
            level = self.__get_StudentEval()
            self.__level = level
        
    def set_AddCredit(self, adding) :
        try :
            adding = int(adding)
        except ValueError :
            print("C'est une chaine de caractere. Veuillez entrez un caractère numérique.")
        if adding >= 0 :
            self.__credit += adding
            self.__level = self.__get_StudentEval()
        else :
            print("Error. La valeur ajoute est inferieur à 0")
    
    def AfficherCredit(self) :
        print(f"Le nombre de crédit de {self.__prenom} {self.__nom} est de {self.__credit} points.")
        
    def __get_StudentEval(self) :
        if self.__credit > 90 :
            return "Excellent"
        elif self.__credit >= 80 :
            return "Très bien"
        elif self.__credit >= 70 :
            return "Bien"
        elif self.__credit >= 60 :
            return "Passable"
        elif self.__credit < 60 :
            return "Insuffisant"
    
    def InfoStudent(self) :
        print(f"Nom = {self.__nom}\nPrénom = {self.__prenom}\nID = {self.__id}\nNiveau = {self.__level}")


student = Student("Doe", "John", 145, 0)
student.set_AddCredit(10)
student.set_AddCredit(10)
student.set_AddCredit(10)
student.AfficherCredit()

### Score Privé ###
student.set_AddCredit(40)
student.InfoStudent()


