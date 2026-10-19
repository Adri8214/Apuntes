def clasificar_stock(stock):
    if stock <= 0:
        return "Agotado"
    elif stock < 5:
        return "Stock bajo"
    elif stock >= 5 and stock <= 10:
        return "Stock suficiente"

stock = int(input("Introduce un número de stock: "))
print(clasificar_stock(stock))