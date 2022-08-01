from servicio.CatalogoPeliculas import CatalogoPeliculas

c = CatalogoPeliculas

n = int(input("Diga que quiere hacer: "))

while n >= 1 and n <= 4:
    if n == 1:
        aniadir = input("A continuacion nombre la pelicula a agregar: ")
        c.agregarPeliculas(aniadir)
        break
    if n == 2:
        c.listarPeliculas()
        break
    if n == 3:
        c.eliminar()
        break
    continue
    
        
