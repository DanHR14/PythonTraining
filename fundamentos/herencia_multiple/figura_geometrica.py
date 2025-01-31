#ABC = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto
    
    def __str__(self):
        return "Ancho: " + str(self.__ancho) + ", alto: " + str(self.__alto)
    
    def get_ancho(self):
        return self.__ancho
    
    def set_ancho(self, ancho):
        self.__ancho = ancho
    
    def get_alto(self):
        return self.__alto
    
    def set_alto(self, alto):
        self.__alto = alto
       
    @abstractmethod 
    def area(self):
        pass