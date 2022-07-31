from unicodedata import name
from Computadora import Computadora
from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton

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
            computadorasStr += computadora.__str__()

        return f'Identificador {self._idOrden}, \nProductos: {computadorasStr}'
    
    @property
    def computadoras(self):
        return self._computadoras
    
    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras

if __name__ == "__main__":   
    monitorRazer = Monitor("razer", 27)
    ratonRazer = Raton("usb", "razer")
    tecladoRazer = Teclado("usb", "razer")
    
    monitorAcer = Monitor("acer", 27)
    ratonHyperx = Raton("usb", "hyperx")
    tecladoHyperx = Teclado("usb", "hyperx")
    
    ratonLogitech = Raton("inalambrico", "logitech")
    
    pcGamer1 = Computadora("PC primer pedido", monitorRazer, tecladoRazer, ratonRazer)
    pcGamer2 = Computadora("PC segundo pedido", monitorAcer, tecladoHyperx, ratonHyperx)
    pcGamer3 = Computadora("PC tercer pedido", monitorAcer, tecladoRazer, ratonLogitech)
    
    pedido1 = [pcGamer1, pcGamer2, pcGamer3]
    print(Orden(pedido1))
        
    
    