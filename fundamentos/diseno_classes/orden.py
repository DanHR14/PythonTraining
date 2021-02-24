class Orden: 
    contador_de_ordenes = 0
    
    def __init__(self, productos):
        Orden.contador_de_ordenes += 1
        self.__id_orden = Orden.contador_de_ordenes
        self.__productos = productos
    
    def __str__(self):
        productos_str = ""
        for producto in self.__productos:
            productos_str += producto.__str__() + " | "
        
        return "Orden: " + str(self.__id_orden) + ", Productos: " + productos_str
    
    def agregar_producto(self, producto):
        self.__productos.append(producto)
        
    
    def get_total(self):
        total = 0
        for producto in self.__productos:
            total += producto.get_precio()
        return total
    
    def get_id_orden(self):
        return __id_orden
    
    def set_id_orden(self, id_orden):
        self.__id_orden = id_orden
    
    def get_productos(self):
        return self.__productos
    
    def set_productos(self, productos):
        self.__productos = productos


    