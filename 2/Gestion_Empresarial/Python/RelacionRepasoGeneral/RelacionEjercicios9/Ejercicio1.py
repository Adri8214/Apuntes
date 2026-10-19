precio = -1

while precio < 0:
    try:
        precio = float(input("Introduce un precio: "))
        if precio < 0:
            print("El precio no puede ser negativo")
    except ValueError:
        print("Debes introducir un número válido")
        precio = -1
print(f"Precio válido: {precio:.2f} EUR")


