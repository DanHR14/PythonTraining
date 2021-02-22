#un diccionario esta compusto por llave,valor (key value)
diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}

print(diccionario)

#largo
print(len(diccionario))

#acceder a un elemento
print(diccionario["IDE"])
#Otra forma, mismo resultado
print(diccionario.get("IDE"))

#Modificar valores
diccionario["IDE"] = "Integrated development environment"
print(diccionario)

#iterar las llaves
for termino in diccionario:
    print(termino)

#iterar los valores con las llaves
for termino in diccionario:
    print(diccionario[termino])

#iterar los valores sin las llaves
for valor in diccionario.values():
    print(valor)

#comprobar existencia de un elemento
print ("IDE" in diccionario)

#agregar nuevos elementos
diccionario["PK"] = "Primary Key"
print(diccionario)

#remover elementos
diccionario.pop("DBMS")
print(diccionario)

#eliminar todos los elementos del diccionario
diccionario.clear()
print(diccionario)

#eliminar por completo el diccionario
del diccionario
print (diccionario)
    