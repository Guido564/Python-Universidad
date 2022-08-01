print("Proporcione los siguientes datos del libro:")

nombre = input("Nombre del libro: ")
id = int(input("ID del libro: "))
precio = float(input("Precio del libro: "))
envio = input("Es el envio gratuito?(True/False) ")

if envio == "True":
    envio = True
elif envio == "False":
    envio == False
else:
    envio = "Valor incorrecto"

# print(nombre)
# print(id)
# print(precio)
# print(envio)

print(f"""
    Nombre: {nombre}
    ID: {id}
    Precio: {precio}
    Envio: {envio}
""")