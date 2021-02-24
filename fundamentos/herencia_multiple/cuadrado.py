from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def __str__(self):
        return FiguraGeometrica.__str__(self) + ", " + Color.__str__(self) + ", "+ str(self.area())
    
    def area(self):
        area = FiguraGeometrica.get_ancho(self) * FiguraGeometrica.get_alto(self)
        return "Area: " + str(area)
    


        