from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRatones = 0
    
    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        Raton.contadorRatones += 1
        self._idRaton = Raton.contadorRatones
    
    def __str__(self):
        return f'Mouse ID {self._idRaton} cuenta con un {super().__str__()}'

if __name__ == "__main__":
    ratonRazer = Raton("usb", "razer")
    print(ratonRazer)
    ratonHyperx = Raton("usb", "hyperx")
    print(ratonHyperx)