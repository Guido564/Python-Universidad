from servicio.CatalogoPeliculas import CatalogoPeliculas

catalogo = CatalogoPeliculas

def menu():
    while(True):
        print("1. Aniadir pelicula")
        print("2. Listar peliculas")
        print("3. Eliminar listado")
        print("4. Salir")
        print()
        
        c = int(input("Seleccione a continuacion que opcione le sienta mejor: "))
        
        if c == 1:
            a = input("Cual pelicula desea aniadir? ")
            catalogo.agregarPelicula(a)
        elif c == 2:
            catalogo.listarPeliculas()
        elif c == 3:
            catalogo.eliminar()
        elif c == 4:
            print("Adios gente")
            exit(0)

menu()
        
