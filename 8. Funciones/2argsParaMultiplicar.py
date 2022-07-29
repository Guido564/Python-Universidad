def multiplicacionAnonima(*args):
    resultado = 1
    for i in args:
        resultado = resultado * i
    return resultado

print(multiplicacionAnonima(2, 100, 10))