def calcular_subtotal(precio, cantidad):
    return precio * cantidad

precio = float(input("Precio: "))
cantidad = int(input("Cantidad:" ))

subtotal = calcular_subtotal(precio, cantidad)

print(f"{subtotal:.2f}")