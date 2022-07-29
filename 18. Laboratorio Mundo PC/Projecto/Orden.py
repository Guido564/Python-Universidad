from unicodedata import name

class Orden:
    contadorOrdenes = 0
    
    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = list(computadoras)
    
    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)
    
    def __str__(self):
        computadorasStr = ''
        for computadora in self._computadoras:
            computadorasStr += computadora.__str__() + '|'

        return f'Identificador: {self._idOrden}, \nProductos: {computadorasStr}'

if __name__ == "__main__":   
    computadora1  = Orden("Soy una pc")
    print(computadora1)
    computadora2  = Orden("Soy otra pc")
    print(computadora2)
        
        
    
    