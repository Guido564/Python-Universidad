from unittest import result


def sumaAnonima(*numeros):
    resultado = 0
    for i in numeros:
        resultado += i
    return resultado
    
    
    

print(sumaAnonima(5, 20, 100))