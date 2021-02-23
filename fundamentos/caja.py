class Caja:
    
    def __init__(self, ancho, largo, alto):
        self.ancho = ancho
        self.largo = largo
        self.alto = alto
        
    def volumen(self):
        return self.ancho * self.largo * self.alto

caja = Caja(2,5,9)
print(caja.volumen()) 