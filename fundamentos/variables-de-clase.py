class MiClase:
    variable_clase = "Variable de clase"
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    
print(MiClase.variable_clase)
objeto1 = MiClase("Variable instancia")
objeto1.variable_clase = "modificada"
print(objeto1.variable_instancia)
print(objeto1.variable_clase)
print(MiClase.variable_clase)

#Podemos Acceder a las variables de clase desde los objetos
print(objeto1.variable_clase)
#Podemos acceder a las variables de clase con el nombre de la clase
print(MiClase.variable_clase)