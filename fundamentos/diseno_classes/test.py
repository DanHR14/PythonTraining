from producto import Producto
from orden import Orden

producto1 = Producto("Camisa" , 10)
producto2 = Producto("Pantalon", 20)
producto3 = Producto("Calcetines", 5)

productos = [producto1, producto2]

orden = Orden(productos)

orden.agregar_producto(producto3)
print(orden)

print(orden.get_total())