class Persona:
    
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.email = email
        
    def __str__(self):
        return (f'Id persona: {self.__id_persona}, '
                f'Nombre: {self.__nombre}, ' 
                f'Apellido: {self.__apellido}, '
                f'Email: {self.__email} '
        )
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self, apellido):
        self.__apellido = apellido
        
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email
    
    def get_id_persona(self):
        return self.__id_persona
    
    
    