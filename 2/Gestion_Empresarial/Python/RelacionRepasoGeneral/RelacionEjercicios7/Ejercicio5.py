categorias = ["hip hop", "soul", "jazz", "soul", "techno"]
productos = ["frigorifico", "horno", "tenedor", "frigorifico", "microondas"]

categorias_unicas = set(categorias)
print(categorias_unicas)

texto = input("Introduce un texto de busqueda: ").strip().lower()

coincidencias = []

for producto in productos:
    if texto in producto.lower():
        coincidencias.append(producto)

print("\n".join(coincidencias))

