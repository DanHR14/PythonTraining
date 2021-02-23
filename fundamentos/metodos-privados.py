class Persona:
    def __init__(self, nombre, primer_apellido, segundo_apellido):
        self.nombre = nombre
        self._primer_apellido = primer_apellido
        self.__segundo_apellido = segundo_apellido

    def metodo_publico(self):
        self.__metodo_privado()
            
    def __metodo_privado(self):
        print(self.nombre)
        print(self._primer_apellido)
        print(self.__segundo_apellido)
        
    def get_primer_apellido(self):
        return self._primer_apellido
    
    def get_segundo_apellido(self):
        return self.__segundo_apellido
    
    def set_primer_apellido(self, primer_apellido):
        self._primer_apellido = primer_apellido
        
    def def_segundo_apellido(self, segundo_apellido):
        self.__segundo_apellido = segundo_apellido
    
p1 = Persona("Juan", "Lopez", "Perez")
p1.metodo_publico()

