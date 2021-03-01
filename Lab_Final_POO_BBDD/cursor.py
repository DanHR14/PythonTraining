from conexion import Conexion
from logger_base import logger

class CursorPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
    
    #Incio de with
    def __enter__(self):
        logger.debug(f'Inicio de with metodo __enter__ {self.__conn}')
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        return self.__cursor
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        logger.debug('Se ejecuta método __exit__()')
        if exception_value:
            self.__conn.rollback()
            logger.debug(f'Ocurrió una excepción: {exception_value}')
        else:
            self.__conn.commit()
            logger.debug('Commit de la transacción')
        #Cerramos el cursor
        self.__cursor.close()
        #Regresamos la conexion al pool
        Conexion.liberarConexion(self.__conn)
        
if __name__ == '__main__':
    #Obtenemos un cursor a partir de la conexion del pool
    #with se ejecuta __enter__ y termina con __exit__
    with CursorPool() as cursor:
        cursor.execute('SELECT * FROM usuarios')
        logger.debug('Listado de personas')
        logger.debug(cursor.fetchall())