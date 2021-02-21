#set es una colección isn orden y sin indices, 
#ni elementos repetidos y los elementos no se pueden modificar
#pero si agregar o eliminar
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

#largo del set
print(len(planetas))

#revisar si un elemento esta en el set
print("Marte" in planetas)

#Agregar elementos
planetas.add("Tierra")

#eliminar arroja excepcion si no existe el elemento en el set
planetas.remove("Tierra")
print(planetas)

#eliminar con discard no arroja excepcion si el elemento no existe en el set
planetas.discard("Tierra")
print(planetas)

#eliminar el contenido del set
planetas.clear()
print(planetas)

#eliminar el set
del planetas
print(planetas)
