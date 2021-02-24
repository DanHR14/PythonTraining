class Color:
    def __init__(self, color):
        self.__color = color
        
    def __str__(self):
        return "Color: " + str(self.__color)
    
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color