class Aritmetica:
    """Clase aritmetica para realizar las operaciones de sumar, restar, etc"""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
        
    def sumar(self):
        """Se realiza la operacion con los atributos de la clase"""
        return self.operando1 + self.operando2
    
#Creamos un nuevo objeto
aritmetica = Aritmetica(2,4)

print("Resultado suma:", aritmetica.sumar())

