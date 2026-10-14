precio = 0.0
dato_valido = 0

while not dato_valido:
    try:
        precio = float(input("Introduce un precio mayor o igual que 0: "))
        dato_valido = precio >= 0
        if not dato_valido:
            print("El precio no puede ser negativo")
    except ValueError:
        print("Introduce un número válido")