from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas

opcion = None
while opcion != 4:
    print("Bienvenido, seleccione una opción")
    print("1. Agregar película")
    print("2. Lista películas")
    print("3. Eliminar Pelicula")
    print("4. Salir")
    opcion = int(input("Seleccione: "))

    if opcion == 1:
        nombre_pelicula = input("Por favor, añada el nombre de la pelicula: ")
        pelicula = Pelicula(nombre_pelicula)
        CatalogoPeliculas.agregar_pelicula(pelicula)
    elif opcion == 2:
        CatalogoPeliculas.listar_peliculas()
    elif opcion == 3:
        CatalogoPeliculas.eliminar()

    