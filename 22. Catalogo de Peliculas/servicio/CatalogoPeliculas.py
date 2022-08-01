import os

class CatalogoPeliculas:
    rutaArchivo = 'peliculas.txt'
    
    def agregarPeliculas(Pelicula):
        print("Ejecutando secuencia")
        rutaArchivo = open('peliculas.txt', 'a')
        rutaArchivo.write(f'{Pelicula}\n')
        print("Secuencia ejecutada con exito")
        rutaArchivo.close()
        
    def listarPeliculas():
        try:
            print("A continuacion las peliculas a listar")
            with open('peliculas.txt') as f:
                print(f.read())
            print("Listado ejecutado con exito")
        except Exception:
            print("No es posible listar las peliculas ya sea porque el archivo fue eliminado o nunca existio en primer lugar")
    
    def eliminar():
        try:
            print("Se van a eliminar las peliculas agregadas")
            os.remove('peliculas.txt')
            print("Se elimino exitosamente")
        except Exception:
            print("El archivo ya se ha eliminado y no puede volverse a eliminar")





