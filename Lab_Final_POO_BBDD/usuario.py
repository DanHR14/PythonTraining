from logger_base import logger

class Usuario:
    def __init__(self, id_usuario = None, username = None, password = None):
        self.__id_usuario = id_usuario
        self.__username = username
        self.__password = password
    
    def __str__(self):
        return (f'ID usuario: {self.__id_usuario}, Username: {self.__username}, Password: {self.__password}')
            
    def get_id_usuario(self):
        return self.__id_usuario
    
    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario
        
    def get_username(self):
        return self.__username
    
    def set_username(self, username):
        self.__username = username
    
    def get_password(self):
        return self.__password
    
    def set_password(self, password):
        self.__password = password
        
if __name__ == '__main__':
    usuario1 = Usuario(1, 'daniel', 123)
    logger.debug(usuario1)