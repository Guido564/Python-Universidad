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
        return f'ID: {self._idComputadoras} Nombre: {self._nombre} Caracteristicas monitor: {self._monitor} Caracteristicas teclado: {self._teclado} Caracteristicas teclado: {self._raton}'
    
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
    pass
    
    
    
        
    