class Monitor:
    contadorMonitores = 0
    
    def __init__(self, marca, tamanio):
        Monitor.contadorMonitores += 1
        self._idComputadoras = Monitor.contadorMonitores
        self._marca = marca
        self._tamanio = tamanio
        pass
    
    def __str__(self):
        return f'Monitor ID {self._idComputadoras} es de marca {self._marca} y tiene un tamanio de {self._tamanio} pulgadas'
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def nombre(self, marca):
        self._marca = marca
        
    @property
    def tamanio(self):
        return self._tamanio
    
    @tamanio.setter
    def nombre(self, tamanio):
        self._tamanio = tamanio

if __name__ == "__main__":   
    monitorGigabyte = Monitor("gigabyte", 27)
    print(monitorGigabyte)
    monitorLG = Monitor("LG", 25)
    print(monitorLG)