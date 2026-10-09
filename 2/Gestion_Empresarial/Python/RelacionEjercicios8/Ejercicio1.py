def calcular_subtotal(precio, cantidad):
    return precio * cantidad

precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

resultado = calcular_subtotal(precio,cantidad)
print (resultado)