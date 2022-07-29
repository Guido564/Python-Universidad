class Producto:
    contadorProductos = 0
    
    def __init__(self, nombre, precio):
        Producto.contadorProductos += 1
        self._idProducto = Producto.contadorProductos
        self._nombre = nombre
        self._precio = precio
        
    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f'Producto [{self._idProducto} {self._nombre} {self._precio}]'

if __name__ == "__main__":    
    producto1 = Producto("Sandia", 250)
    print(producto1)
    producto2 = Producto("Harina", 170)
    print(producto2)
    producto3 = Producto("Aceite", 120)
    print(producto3)
    