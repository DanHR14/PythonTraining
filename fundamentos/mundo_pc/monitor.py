class Monitor:
    CONTADOR_MONITORES = 0
    
    def __init__(self, marca, tamanio):
        Monitor.CONTADOR_MONITORES += 1
        self.__id_monitor = Monitor.CONTADOR_MONITORES
        self.__marca = marca
        self.__tamanio = tamanio
    
    def __str__(self):
        return (
            f"ID: {self.__id_monitor}, "
            f"Marca {self.__marca}, "
            f"Tamanio {self.__tamanio}"
        )