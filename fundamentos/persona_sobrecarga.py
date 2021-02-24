class Persona:
    
    def __init__(self, nombre):
        self.__nombre = nombre
    
    #Metodo sobreescrito de la clase padre object
    def __add__(self, otro):
        return self.__nombre + " " + otro.__nombre
    
    def __sub__(self, otro):
        return "Operador no soportado"
    
p1 = Persona("Juan")
p2 = Persona("Carla")

print(p1 + p2)