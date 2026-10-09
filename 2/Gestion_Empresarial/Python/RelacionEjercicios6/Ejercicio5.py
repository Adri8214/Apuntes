numero_productos = int(input("Introduce un número de productos: "))
numero_meses = int(input("Introduce un número de meses: "))

lineas = []

for numero in range(1,numero_productos + 1):
    for meses in range(1,numero_meses + 1):
        lineas.append(f"Producto{numero} - Mes{meses}")
print("\n".join(lineas))