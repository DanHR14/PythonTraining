import psycopg2

conexion = psycopg2.connect(user="postgres", 
                 password="admin", 
                 host="127.0.0.1",
                 port="5432",
                 database="test_db")

cursor = conexion.cursor()
sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"
valores = (
    ('Marcos', 'Jimenez', 'mjimenez@gmail.com'),
    ('Angel', 'Quintana', 'aquintana@gmail.com'),
    ('Maria', 'Gonzalez', 'mgonzalez@gmail.com')
)

cursor.executemany(sentencia, valores)
#guardar la info en la base de datos
conexion.commit()
registros_insertados = cursor.rowcount
print(f"Registros insertados: {registros_insertados}")
cursor.close()
conexion.close()