class Producto:
    contador_productos = 0
    
    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self.__id_producto = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio
    
    def __str__(self):
        return "ID: {}, Nombre: {}, Precio: {}".format(self.__id_producto, self.__nombre, self.__precio)
    
    def get_id_producto(self):
        return self.__id_producto
    
    def set_id_producto(self, id_producto):
        self.__id_producto = id_producto
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio
    
        
