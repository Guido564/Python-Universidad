import os

class CatalogoPeliculas:
    rutaArchivo = 'peliculas.txt'
    
    def agregarPeliculas(Pelicula):
        rutaArchivo = open('peliculas.txt', 'a')
        rutaArchivo.write(f'{Pelicula}\n')
        rutaArchivo.close()
    
    def listarPeliculas():
        with open('peliculas.txt') as f:
            print(f.read())
    
    def eliminar():
        os.remove('peliculas.txt')
    
    
h = CatalogoPeliculas
h.eliminar()




