from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    CONTADOR_TECLADOS = 0
    
    def __init__(self, tipo_entrada, marca):
        Teclado.CONTADOR_TECLADOS += 1
        self.__id_teclado = Teclado.CONTADOR_TECLADOS
        self._tipo_entrada = tipo_entrada
        self._marca = marca
    
    def __str__(self):
        return (
            f"ID: {self.__id_teclado},"
            f"marca: {self._marca}, "
            f"tipo_entrada: {self._tipo_entrada}"      
        )