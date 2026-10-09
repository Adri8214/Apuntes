def clasificar_stock(stock):
    if stock == 0:
        print("Agotado")
    elif stock < 5:
        print("Stock bajo")
    elif stock >=5 and stock <= 9:
        print("stock suficiente")
    else:
        print("Introduce un número entre 0 y 10")
    return stock

print (clasificar_stock(8))
