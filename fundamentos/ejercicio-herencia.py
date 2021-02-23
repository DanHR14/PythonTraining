class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "Color: " + str(self.color) + ", ruedas: " + str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return super().__str__() + ", velocidad: " + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + ", tipo: " + str(self.tipo)
    
vehiculo = Vehiculo("rosa", 2)
print(vehiculo)

coche = Coche("negro", 4, 76.5)
print(coche)

bicicleta = Bicicleta("gris", 2, "montaña")
print(bicicleta)
      