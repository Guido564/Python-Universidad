from dominio.Pelicula import Pelicula
import os

class CatalogoPeliculas:
    archivo = open('pelicula.txt', 'w')
    
    def agregarPelicula(Pelicula):
        with open('pelicula.txt', 'a') as adicionPelicula:
            adicionPelicula.write(f'{Pelicula}\n')

    def listarPeliculas():
        archivo = open('pelicula.txt', 'r')
        for linea in archivo:
            print(linea)
    
    def eliminar():
        os.remove('peliculas.txt')


    