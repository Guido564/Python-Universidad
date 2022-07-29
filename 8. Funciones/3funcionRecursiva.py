def recursividad(numero):
    if numero < 1:
        return 1
    else:
        print(numero)
        recursividad(numero - 1)
    
    
recursividad(4)