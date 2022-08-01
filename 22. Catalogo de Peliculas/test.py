from servicio.CatalogoPeliculas import CatalogoPeliculas
from dominio.Pelicula import Pelicula

catalogo = CatalogoPeliculas

def menu():
    while(True):
        try:
            print("1. Aniadir pelicula")
            print("2. Listar peliculas")
            print("3. Eliminar listado")
            print("4. Salir")
            print()
            
            c = int(input("Seleccione a continuacion que opcione le sienta mejor: "))
            
            if c == 1:
                a = input("Cual pelicula desea aniadir? ")
                pelicula = Pelicula(a)
                catalogo.agregarPelicula(pelicula)
            elif c == 2:
                catalogo.listarPeliculas()
            elif c == 3:
                catalogo.eliminar()
            elif c == 4:
                print("Adios gente")
                exit(0)
        except Exception:
            print("Eliga un caracter valido porque de otro modo programa boom")

menu()
        
