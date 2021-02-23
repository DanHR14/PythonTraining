class Persona:
    
    def __init__(self, n):
        self.__nombre = n
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, n):
        self.__nombre = n
    
p1 = Persona("Juan")
print(p1.get_nombre())

p1.set_nombre("Karla")
print(p1.get_nombre())