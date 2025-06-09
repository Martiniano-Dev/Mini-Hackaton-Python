papitas = {
    "nombre": "Papitas",
    "precio": 10
}

juguito = {
    "nombre": "Juguito",
    "precio": 800
}
alfajor = {
    "nombre": "Alfajor",
    "precio": 11
}

print("")
print("< TIENDA ESCOLAR >")
print("")
print("Te damos al bienvenida a la tienda escolar, no te estafaremos.")
print("")
print("Productos:")
print("- Juguito: $800")
print("- Papitas: $10")
print("- Alfajor: $11")
print("")

print("Escribe el nombre de los productos para añadirlo al carrito, escribe 'Listo' para terminar y recibir el precio total.")
print("")

sumatotal = 0

while True:
    eleccion = input("Escribe: ")
    if eleccion.lower() == "listo":
        break
    if eleccion.lower() == "papitas":
        sumatotal += papitas["precio"]
        print("< Agregaste papitas >")
    elif eleccion.lower() == "juguito":
        sumatotal += juguito["precio"]
        print("< Agregaste juguito >")
    elif eleccion.lower() == "alfajor":
        sumatotal += alfajor["precio"]
        print("< Agregaste alfajor >")
    else:
        print("< No es una opción válida >")

print("")
print("El total es:", sumatotal, "pesos")
print("")
