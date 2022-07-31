from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclados = 0
    
    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        Teclado.contadorTeclados += 1
        self._idTeclado = Teclado.contadorTeclados
    
    def __str__(self):
        return f'Teclado ID {self._idTeclado} cuenta con un {super().__str__()}'

if __name__ == "__main__":   
    tecladoRazer = Teclado("usb", "razer")
    print(tecladoRazer)
    tecladoHyperx = Teclado("usb", "hyperx")
    print(tecladoHyperx)