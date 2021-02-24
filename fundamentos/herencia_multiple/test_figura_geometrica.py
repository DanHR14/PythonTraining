from cuadrado import Cuadrado
from figura_geometrica import FiguraGeometrica
from rectangulo import Rectangulo

#No se puede crear objetos de una clase abstracta
#figuraGeometrica = FiguraGeometrica()

cuadrado = Cuadrado(2, "Rojo")
print(cuadrado)

rectangulo = Rectangulo(2, 4, "Azul")
print(rectangulo)