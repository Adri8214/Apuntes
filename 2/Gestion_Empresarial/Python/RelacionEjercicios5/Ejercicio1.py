nombre_producto = input("Introduce el nombre del producto: ")
stock = int(input("Introduce el stock del producto: "))

if stock < 0:
    print("El stock es negativo")
elif stock == 0:
    print("Agotado")
elif stock < 5:
    print("Stock bajo")
else:
    print("Stock suficiente")