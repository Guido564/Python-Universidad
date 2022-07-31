from Monitor import *
from Raton import *
from Teclado import *
from DispositivoEntrada import *

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
        return f'ID {self._idComputadoras} Caracteristicas \nNombre: {self._nombre} \nCaracteristicas monitor: {self._monitor} \nCaracteristicas teclado: {self._teclado} \nCaracteristicas teclado: {self._raton}'
    
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
    monitorRazer = Monitor("razer", 27)
    print(monitorRazer)
    ratonRazer = Raton("usb", "razer")
    print(ratonRazer)
    tecladoRazer = Teclado("usb", "razer")
    print(tecladoRazer)
    
    pcRazer = Computadora("PC full Razer", monitorRazer, tecladoRazer, ratonRazer)
    print(pcRazer)
    
    monitorHP = Monitor("HP", 22)
    print(monitorRazer)
    ratonGenerico = Raton("usb", "generica")
    print(ratonGenerico)
    tecladoGenerico = Teclado("usb", "generica")
    print(tecladoGenerico)
    
    pcOficina = Computadora("PC de Oficina", monitorHP, tecladoGenerico, ratonGenerico)
    print(pcOficina)
    
    
        
    