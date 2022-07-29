from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho):
        self._ancho = ancho
        self._alto = alto
        
    
    def __str__(self):
        return f'La figura tiene un ancho de {self._ancho} y un alto de {self._alto}'
    
    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        self._alto = alto
    
    @property
    def ancho(self):
        return self._ancho
    
    @alto.setter
    def ancho(self, ancho):
        self._ancho = ancho
        
    @abstractmethod
    def calcularArea(self):
        pass

if __name__ == "__main__":
    figura1 = FiguraGeometrica(10, 20)
    print(figura1)
    
    