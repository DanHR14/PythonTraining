import psycopg2

conexion = psycopg2.connect(user="postgres",
                            password="admin",
                            host="127.0.0.1",
                            port="5432",
                            database="test_db")

cursor = conexion.cursor()
sentencia = "DELETE FROM persona WHERE id_persona IN %s"

entrada = input("Proporciona las pks a eliminar (seguido de comas): ")
tupla = tuple(entrada.split(','))
valores = (tupla,)

cursor.execute(sentencia, valores)
conexion.commit()
registros_eliminados = cursor.rowcount
print(f"Registros insertados: {registros_eliminados}")
cursor.close()
conexion.close()

