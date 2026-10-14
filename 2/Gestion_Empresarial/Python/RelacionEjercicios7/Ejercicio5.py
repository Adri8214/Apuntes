categorias = ["piano", "guitarra", "ukelele", "piano", "tambor", "bajo"]
productos = ["piano digital", "objetivo", "obturador", "carrete", "camara analogica"]

categorias_unicas = set(categorias)
print(categorias_unicas)

texto_busqueda = input("Texto de busqueda: ").strip().lower()

coincidencias = []

for producto in productos:
    if texto_busqueda in producto.lower():
        coincidencias.append(producto)

print("\n".join(coincidencias))