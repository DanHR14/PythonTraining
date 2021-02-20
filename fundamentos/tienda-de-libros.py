print("Proporcione los siguientes datos del libro:")

nombre = input("Proporiona el nombre:")
id = int(input("Proporciona el ID:"))
precio = float(input("Proporciona el precio:"))
envioGratuito = input("Indica si el envio es gratuito (True/False")

if envioGratuito == "True" :
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto, debe ser True/False"

print("Nombre:", nombre)
print("Id:", id)
print("Precio:", precio)
print("Envio Gratuito?:", envioGratuito) 