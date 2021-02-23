class Persona:
    
    def __init__(this, nombre, edad, *v, **d):
        this.nombre = nombre
        this.edad = edad
        this.valores = v
        this.diccionario = d
        
    def desplegar(this):
        print("Nombre: ", this.nombre)
        print("Edad", this.edad)
        print("Valores (Tupla):", this.valores)
        print("Diccionario: ", this.diccionario)
        
p1 = Persona("Juan", 20)
p1.desplegar()

p2 = Persona("Carla", 30, 2,4,5)
p2.desplegar()

p3 = Persona("Paula,", 33, 4,9, m="manzana", p="pera")
p3.desplegar()