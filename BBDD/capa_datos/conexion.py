from logger_base import logger
import psycopg2 as db
import sys


class Conexion:
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __conexion = None
    __cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion = db.connect(host=cls.__HOST,
                                            user=cls.__USERNAME,
                                            password=cls.__PASSWORD,
                                            port=cls.__DB_PORT,
                                            database=cls.__DATABASE)
                logger.debug(f'Conexion existosa: {cls.__conexion}')
                return cls.__conexion
            except Exception as e:
                logger.error(f'Error al conectar a la Base de datos {e}')
                sys.exit()
        else:
            return cls.__conexion

    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.__conexion.cursor()
                logger.debug(f'Se ha establecido el cursor: {cls.__cursor}')
            except Exception as e:
                logger.error(f"Error al establecer el cursor {e}")
                sys.exit()
        else:
            return cls.__cursor

    @classmethod
    def cerrar(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
                logger.debug(f'Se ha cerrado el cursor: {cls.__cursor}')
            except Exception as e:
                logger.error(f'Error al cerrar el cursor {e}')
                sys.exit
        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
                logger.debug(f'Se ha cerrado la conexion: {cls.__conexion}')
            except Exception as e:
                logger.error(f'Error al cerrar la conexión: {e}')
        logger.debug("Se han cerrado todos los objetos de conexion y cursor")


if __name__ == '__main__':
    logger.info('desde conexion')
