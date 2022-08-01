diccionario = {
    "HTML":"HyperText Markup Language",
    "CSS":"cascade style sheet",
    "JavaScript":"Lenguaje Orientado a Objetos"
}

print(diccionario)

print(len(diccionario))

print(diccionario["CSS"])

print(diccionario.get("HTML"))

diccionario["JavaScript"] = "Utilizado en paginas web"
print(diccionario["JavaScript"])