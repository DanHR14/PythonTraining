from logger_base import logger
from usuarioDAO import UsuarioDao
from usuario import Usuario

opcion = None
while opcion != '5':
    print('Opciones')
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Actualizar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    
    opcion = input('Por favor, elija una opción: ')
    
    def listar_usuarios():
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            print(usuario)        
        
    def agregar_usuario():
        username_var = input('Escriba el username: ')
        password_var = input('Escriba el password: ')
        usuario = Usuario(username=username_var, password=password_var)
        UsuarioDao.insertar(usuario)
        
    def actualizar_usuario():
        idUsuario = input('Indiquie el ID del usuario que quiere actualizar: ')
        username_var = input('Introduzca el nombre del nuevo usuario: ')
        password_var = input('Introduzca el nuevo password:') 
        usuario = Usuario(idUsuario, username_var, password_var)
        UsuarioDao.actualizar(usuario)
        
    def eliminar_usuario():
        idUsuario = input('Indique el ID del usuario que quiere eliminar: ')
        usuario = Usuario(id_usuario=idUsuario)
        UsuarioDao.eliminar(usuario)
        
    if opcion == '1':
        listar_usuarios()
    elif opcion == '2':
        agregar_usuario()
    elif opcion == '3':
        actualizar_usuario()
    elif opcion == '4':
        eliminar_usuario()
        
    
    