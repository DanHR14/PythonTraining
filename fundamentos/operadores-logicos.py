a = int(input("Proporciona un valor:"))
valorMinimo = 0
valorMaximo = 5
dentroRango = (a >= valorMinimo and a <= valorMaximo)
fueraRango =  (a >= valorMinimo or a <= valorMaximo)
#print(dentroRango)
if not(dentroRango) :
    print("fuera de rango")
else:
    print("dentro de rango")

