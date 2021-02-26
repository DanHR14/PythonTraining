import psycopg2

conexion = psycopg2.connect(user="postgres", 
                 password="admin", 
                 host="127.0.0.1",
                 port="5432",
                 database="test_db")

try:
    #conexion.autocommit = True
    cursor = conexion.cursor()
    sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"
    valores = ('Carlos', 'Lara', 'clara@gmail.com')
    cursor.execute(sentencia, valores)

    sentencia = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
    valores = ('Juan', 'Perez', 'jperez@gmail.com', 4)
    cursor.execute(sentencia, valores)

    #guardar la info en la base de datos
    conexion.commit()
    registros_insertados = cursor.rowcount
    print(f"Registros insertados: {registros_insertados}")
except Exception as e:
    conexion.rollback()
    print(f"Ocurrio un error en la transaccion {e}")
finally:
    cursor.close()
    conexion.close()