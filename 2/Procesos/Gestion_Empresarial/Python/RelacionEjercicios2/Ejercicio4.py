nombre_producto = input("Introduce el nombre del producto")
existencias_iniciales = int(input("Introduce el numero de existencias iniciales: "))
unidades_recibidas = int(input("Introduce el número de unidades recibidas: "))
unidades_vendidas = int(input("Introduce el número de unidades vendidas: "))

stockFinal = existencias_iniciales + unidades_recibidas - unidades_vendidas

print(f"{nombre_producto}\nUnidades iniciales: {existencias_iniciales}\nUnidades recibidas: {unidades_recibidas}\nUnidades vendidas: {unidades_recibidas}\nUnidades restantes: {stockFinal}")