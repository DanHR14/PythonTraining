from logger_base import logger
from conexion import Conexion
from persona import Persona


class PersonaDao:
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    __ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    __ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):
        cursor = Conexion.obtenerCursor()
        logger.debug(cursor.mogrify(cls.__SELECCIONAR))
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            persona = Persona(registro[0], registro[1],
                              registro[2], registro[3])
            personas.append(persona)
        Conexion.cerrar()
        return personas

    @classmethod
    def insertar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar {persona}')
            valores_persona = (persona.get_nombre(),
                               persona.get_apellido(), persona.get_email())
            cursor.execute(cls.__INSERTAR, valores_persona)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepcion al insertar persona: {e}')
        finally:
            Conexion.cerrar()

    @classmethod
    def actualizar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            valores_persona = (persona.get_nombre(), persona.get_apellido(), 
                               persona.get_email(), persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR, valores_persona)
            conexion.commit()
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepcion al actualizar persona {e}')
        finally:
            Conexion.cerrar()
            
    @classmethod
    def eliminar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            valores = (persona.get_id_persona(),)
            cursor.execute(cls.__ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepcion al eliminar')
        finally:
           Conexion.cerrar()


if __name__ == '__main__':
   
#    persona = Persona(id_persona=2)
#    personas_eliminadas = PersonaDao.eliminar(persona)
#    logger.debug(f'Personas eliminadas: {personas_eliminadas}')
    persona = Persona(nombre='Pedro', apellido='Najera', email='pnajera@mail.com')
    personas_insertadas = PersonaDao.insertar(persona)
    logger.debug(f'Personas insertados: {personas_insertadas}')