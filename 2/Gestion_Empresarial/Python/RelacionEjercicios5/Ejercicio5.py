venta_tienda = float(input("Introduce las ventas de la tienda: "))
venta_web = float(input("Introduce las ventas de la web: "))
venta_telefono = float(input("Introduce las ventas del teléfono: "))

maximo = max(venta_tienda, venta_web, venta_telefono)
empate = 0

if venta_tienda == maximo:
    empate += 1
if venta_web == maximo:
    empate += 1
if venta_telefono == maximo:
    empate += 1

if empate > 1:
    print("Empate")
elif venta_tienda == maximo:
    print("Tienda")
elif venta_web == maximo:
    print("Web")
else:
    print("Teléfono")