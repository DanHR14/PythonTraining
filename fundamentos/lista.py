nombres = ["juan", "carla", "ricardo", "maria"]
print(nombres)

#conocer el largo de la lista
print(len(nombres))

#Acceder al elemento 0
print(nombres[0])
print(nombres[1])

#Navegación Inversa
print(nombres[-1])
print(nombres[-2])

#imprimir rango
print(nombres[0:2]) #sin incluir el indice 2

#imprimir los elementos de inicio hasta el indice proporcionado
print(nombres[:3]) #sin incluir el indice 3

#imprimir los elementos hasta el final desde el indice proporcionado
print(nombres[1:])

#Cambiar los elementos de una lista
nombres[3] = "Ivone"
print(nombres)

#Iterar lista
for nombre in nombres:
    print(nombre)
    
#Revisar si existe un elemento en la lista
if "carla" in nombres:
    print("carla existe en la lista")
else:
    print("el elemento buscado no existe en la lista")

#agregar un nuevo elemento
nombres.append("Lorenzo")
print(nombres)

#insertar un nuevo elemento en el indicie proporcionado
nombre.insert(1, "Octavio")
print(nombres)

#borrar un elemento
nombre.remove("Octavio")
print(nombres)

#remover el ultimo elemento de nuestra lista
nombres.pop()
print(nombres)

#borrar el indice indicado de la lista
del nombres[0]
print(nombres)

#limpiar todos los elementos de la lista
nombres.clear()
print(nombres)

#eliminar por completo la lista
del nombres
print(nombres)
