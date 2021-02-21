nota = float(input("Proporciona un valor entre 0 y 10:"))
Calificacion = None

if nota >= 9 or nota <= 10:
    Calificacion = "A"
elif nota >= 8 or nota < 9:
    Calificacion = "B"
elif nota >= 7 or nota < 8:
    Calificacion = "C"
elif nota >= 6 or nota < 7:
    Calificacion = "D"
elif nota >= 0 or nota < 6:
    Calificacion = "F"
else:
    Calificacion = "Valor incorrecto"

print(Calificacion)