numero_productos = int(input("Introduce un número de prodcutos: "))
numero_meses = int(input("Introduce un numero de meses: "))

lineas = []

for productos in range(1,numero_productos + 1):
    for meses in range(1,numero_meses + 1):
        lineas.append(f"Producto {productos} - Mes {meses}")

print("\n".join(lineas))