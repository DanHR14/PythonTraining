class Orden:
    CONTADOR_ORDENES = 0
    
    def __init__(self, computadoras):
        Orden.CONTADOR_ORDENES += 1
        self.__id_orden = Orden.CONTADOR_ORDENES
        self.__computadoras = computadoras
    
    def agregar_computadora(self, computadora):
        self.__computadoras.append(computadora)
    
    def __str__(self):
        computadoras_str = ""
        for computadora in self.__computadoras:
            computadoras_str += computadora.__str__()
        
        return (
            f"Orden: {self.__id_orden}"
            f"Computadoras: {computadoras_str}"
        )    