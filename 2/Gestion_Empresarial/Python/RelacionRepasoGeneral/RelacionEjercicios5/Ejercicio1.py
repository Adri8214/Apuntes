nombre_producto = input("Nombre producto: ")
stock = int(input("Stock producto: "))

if stock == 0:
    print("Agotado")
elif stock >= 1 and stock <= 5:
    print("Stock bajo")
elif stock > 5:
    print("Stock suficiente")
else:
    print("Introduce un número positivo")