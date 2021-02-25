import psycopg2

conexion = psycopg2.connect(user="postgres", 
                 password="admin", 
                 host="127.0.0.1",
                 port="5432",
                 database="test_db")

cursor = conexion.cursor()
sentencia = "SELECT * FROM persona WHERE id_persona IN %s"
entrada = "1,2,3" #input("Proporciona las pk a buscar (separado por comas): ")
tupla = tuple(entrada.split(','))
llaves_primarias = (tupla,)
#id_persona = input("Proporciona la pk a buscar: ")
cursor.execute(sentencia, llaves_primarias)
registros = cursor.fetchall()
for registro in registros:
    print(registro)

cursor.close()
conexion.close()