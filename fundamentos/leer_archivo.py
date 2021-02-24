#en MAC y linux no hace falta el doble \\ ya que usa / lo dejamos asi

try:
    archivo = open("C:\\Users\\danie\\OneDrive\\Escritorio\\formaciones\\Python\\fundamentos\\prueba.txt", "r")
    print(archivo.read())
    
    #lee solo 5 caracteres
    print(archivo.read(5))
    #lee los siguientes 3 caracteres de donde se ha quedado el anterior read
    print(archivo.read(3))
    
    #leer una sola linea
    print(archivo.readline())
    print(archivo.readline())
    
    #iterar lectura de lineas
    for linea in archivo:
        print(linea)
        
    #leer lineas
    print(archivo.readlines())
    
    #acceder a una linea de la lista
    print(archivo.readlines()[1])
    
    #abrimos un nuevo archivo
    #anexamos informacion a nuestro archivo
    archivo2 = open("copia.txt", "a")
    
    archivo2 = open("copia.txt", "w")
    #copiar el archivo 1 al archivo 2
    archivo2.write(archivo.read())
    
except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()