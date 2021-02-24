class MiClase:
    
    variable_clase = "Variable clase"
    
    def __init__(self):
        self.variable_instancia = "Variable Instancia"
    
    @staticmethod
    def metodo_estatico():
        print("metodo estatico")
        print(MiClase.variable_clase)
        
    @classmethod
    def metodo_clase(cls):
        print("Metodo de clase: " + str(cls))
        print(cls.variable_clase)
        
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico() 
        

MiClase.metodo_estatico()
MiClase.metodo_clase()      
 
print()

objeto = MiClase()
objeto.metodo_instancia()