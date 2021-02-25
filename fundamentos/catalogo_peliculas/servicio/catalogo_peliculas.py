import os

class CatalogoPeliculas:
    RUTA_ARCHIVO = "C:\\Users\\danie\\OneDrive\\Escritorio\\formaciones\\Python\\fundamentos\\catalogo_peliculas\\peliculas.txt"
    
    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            archivo = open(CatalogoPeliculas.RUTA_ARCHIVO, "a+")
            archivo.write(pelicula.__str__() + "\n")
        except Exception as e:
            print("Hubo un error al agregar una nueva pelicula")
        finally:
            archivo.close()
            print("Se agrega ", pelicula)
        
    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.RUTA_ARCHIVO, "r")
            print("Catálogo de Películas:")
            print(archivo.read())
        except Exception as e:
            print("Hubo un error al listar las peliculas")
        finally:
            archivo.close()
    
    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.RUTA_ARCHIVO)
            print("archivo eliminado: ", CatalogoPeliculas.RUTA_ARCHIVO)
        except Exception as e:
            print("Hubo un error al eliminar el catalogo", e)
            
        
            
   
        