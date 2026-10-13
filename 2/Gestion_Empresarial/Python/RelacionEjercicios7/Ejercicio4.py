productos = [
{"Nombre": "Ratón", "Categoría": "Periféricos", "Precio": 15, "Stock": 5},
{"Nombre": "Televisión", "Categoría": "Vídeo y Sonido", "Precio": 200, "Stock": 90},
{"Nombre": "Boli", "Categoría": "Papelería", "Precio": 2, "Stock": 20},
{"Nombre": "Cuchara", "Categoría": "Utensilios", "Precio": 3.5, "Stock": 37}
]

linea = []
disponibles = 0

for producto in productos:
    if producto["Stock"] > 0:
        linea.append(producto["Nombre"])
        disponibles += 1

linea.append(f"Disponibles: {disponibles}")

print("\n".join(linea))