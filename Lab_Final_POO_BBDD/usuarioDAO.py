from usuario import Usuario
from logger_base import logger
from cursor import CursorPool

class UsuarioDao:
    __SELECCIONAR = 'SELECT * FROM usuarios ORDER BY id_usuario'
    __INSERTAR = 'INSERT INTO usuarios(username, password) VALUES(%s,%s)'
    __ACTUALIZAR = 'UPDATE usuarios SET username=%s, password=%s WHERE id_usuario=%s'
    __ELIMINAR = 'DELETE FROM usuarios where id_usuario=%s'
    
    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuarios.append(Usuario(registro[0], registro[1], registro[2]))
            return usuarios
        
    @classmethod
    def insertar(cls, usuario):
        with CursorPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            valores = (usuario.get_username(), usuario.get_password())
            cursor.execute(cls.__INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, usuario):
        with CursorPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            valores = (usuario.get_username(), usuario.get_password(), usuario.get_id_usuario())
            cursor.execute(cls.__ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, usuario):
        with CursorPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            valores = (usuario.get_id_usuario(),)
            cursor.execute(cls.__ELIMINAR, valores)
            return cursor.rowcount
            
            

if __name__ == '__main__':

    #Insertamos un nuevo registro
    #usuario = Usuario(username='Ramon', password='542')
    #usuario_insertado = UsuarioDao.insertar(usuario)
    #logger.debug(f'usuario añadido: {usuario_insertado}')

    #usuarios = UsuarioDao.seleccionar()
    #for usuario in usuarios:
    #    logger.debug(usuario)

    # Actualizar un registro existente
    #usuario = Usuario('4','Juan','798')
    #usuario_actualizado = UsuarioDao.actualizar(usuario)
    #logger.debug(f'usuarios actualizados: {usuario_actualizado}')
    
    #eliminar un registro existente
    usuario = Usuario(id_usuario=3)
    usuarios_eliminadas = UsuarioDao.eliminar(usuario)
    logger.debug(f'Usuarios eliminadas: {usuarios_eliminadas}')