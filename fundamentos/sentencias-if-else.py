numero = int(input("Proporciona un número entre 1 y 3: "))

if numero == 1:
    numeroTexto = "número uno"
elif numero == 2:
    numeroTexto = "número dos"
elif numero == 3:
    numeroTexto = "número tres"
else:
    numeroTexto = "Valor fuera de rango"

print("numero proporcionado:", numeroTexto)    
