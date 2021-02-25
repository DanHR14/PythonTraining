class Computadora:
    CONTADOR_COMPUTADORAS = 0
    
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.CONTADOR_COMPUTADORAS += 1
        self.__id_computadora = Computadora.CONTADOR_COMPUTADORAS
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton
    
    def __str__(self):
        return (
            f"""
            {self.__nombre}: {self.__id_computadora} 
                Monitor: {self.__monitor}
                Teclado: {self.__teclado} 
                Ratón: {self.__raton}
                """
        )