import psycopg2

conexion = psycopg2.connect(user="postgres", 
                 password="admin", 
                 host="127.0.0.1",
                 port="5432",
                 database="test_db")

cursor = conexion.cursor()
sentencia = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
valores = ('Juan1', 'Perez2', 'jperez3@gmail.com', 1)
cursor.execute(sentencia, valores)
#guardar la info en la base de datos
conexion.commit()
registros_actualizados = cursor.rowcount
print(f"Registros insertados: {registros_actualizados}")
cursor.close()
conexion.close()