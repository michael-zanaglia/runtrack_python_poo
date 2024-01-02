class Operation:
    def __init__(self, nombre1, nombre2):
        self.n1 = nombre1
        self.n2 = nombre2
    def AfficherNombre(self) :
        print(f"Le nombre1 est {self.n1}.")
        print(f"Le nombre2 est {self.n2}.")
    def Addition(self):
        print(self.n1 + self.n2)
        
operation = Operation(12, 3)
operation.AfficherNombre()
operation.Addition()