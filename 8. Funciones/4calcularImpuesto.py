pagoSinImpuesto = int(input("Ingrese el pago sin impuesto: "))
impuesto = int(input("Ingrese el impuesto: "))

def calcularImpuesto(pagoSinImpuesto, impuesto):
    pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
    return f'El pago con impuestos seria de un total de: {pagoTotal}'

print(calcularImpuesto(pagoSinImpuesto, impuesto))