from numeros_identicos_exception import NumerosIdenticosException
resultado = None


try:
    a = int(input("Primer número: "))
    b = int(input("Segundo número:"))
    if a == b:
        raise NumerosIdenticosException("Ocurrio un error, numeros identicos")
    resultado = a/b
except ZeroDivisionError as e:
    print("Ocurrio un error con ZeroDivisionError: ", e)
    print(type(e))
except TypeError as e:
    print("Ocurrio un error con TypeError", e)
    print(type(e))
except ValueError as e:
    print("Ocurrio un error con ValueError: ", e)
#Excepcion de alto nivel (para todo)
except Exception as e:
    print("Ocurrio un error con exception: ", e)
    print(type(e))
#Solo saltara cuando haya excepcion
else:
    print("No hubo ninguna excepcion")
#siempre se ejecutara aun que salte excepcion
finally:
    print("fin del manejo de excepciones")

print("resultado: ", resultado)
print("Despues de la ejecucion del error sigue trabajando")
