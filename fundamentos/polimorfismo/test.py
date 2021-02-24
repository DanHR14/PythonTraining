from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto), end="\n\n")
    if isinstance(objeto, Gerente):
        print(objeto.departamento)
        
    
empleado = Empleado("Juan", 1000)
imprimir_detalles(empleado)

empleado = Gerente("Carla", 2000, "IT")
imprimir_detalles(empleado)