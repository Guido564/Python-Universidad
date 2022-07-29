class Computadora:
    contadorComputadoras = 0
    
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self._idComputadoras = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    
    def __str__(self):
        return f'{self._idComputadoras} {self._nombre} {self._monitor} {self._teclado} {self._raton}'
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def monitor(self):
        return self._monitor
    
    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor
    
    @property
    def teclado(self):
        return self._teclado
    
    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado
        
    @property
    def raton(self):
        return self._raton
    
    @raton.setter
    def raton(self, raton):
        self._raton = raton
    
if __name__ == "__main__":   
    computadora1  = Computadora("Soy una pc", 1, 2, 3)
    print(computadora1)
    computadora2  = Computadora("Soy una pc", 1, 2, 3)
    print(computadora2)
    
    
    
        
    