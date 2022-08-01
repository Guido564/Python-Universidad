import os
from dominio import Pelicula

class CatalogoPeliculas:
    rutaArchivo = 'peliculas.txt'
    
    
    @classmethod
    def agregarPelicula(cls, pelicula):
        print("Ejecutando secuencia")
        with open(cls.rutaArchivo, 'a') as a:
            a.write(f'{pelicula}\n')
        print("Secuencia ejecutada con exito")
        
    @classmethod
    def listarPeliculas(cls):
        try:
            print("A continuacion las peliculas a listar")
            with open(cls.rutaArchivo, 'r') as f:
                print(f.read())
            print("Listado ejecutado con exito")
        except Exception:
            print("No es posible listar las peliculas ya sea porque el archivo fue eliminado o nunca existio en primer lugar")
        
    @classmethod
    def eliminar(cls):
        try:
            print("Se van a eliminar las peliculas agregadas")
            os.remove(cls.rutaArchivo)
            print("Eliminacion exitosa")
        except Exception:
            print("El archivo ya se ha eliminado (o nunca existio) y no puede volverse a eliminar")





