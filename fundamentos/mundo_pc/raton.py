from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    CONTADOR_RATONES = 0
    
    def __init__(self, tipo_entrada, marca):
        Raton.CONTADOR_RATONES += 1
        self.__id_raton = Raton.CONTADOR_RATONES
        self._marca = marca
        self._tipo_entrada = tipo_entrada
        
    def __str__(self):
        return (
            f"Id: {self.__id_raton}, "
            f"marca: {self._marca}, "
            f"tipo_entrada: {self._tipo_entrada}"            
        )
    
    