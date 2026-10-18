ventas_tienda = float(input("Ventas de tienda: "))
ventas_web = float(input("Ventas de web: "))
ventas_telefono = float(input("Ventas de telefono: "))

maximo = max(ventas_tienda, ventas_web, ventas_telefono)
empates = 0

if ventas_tienda == maximo:
    empates += 1
if ventas_web == maximo:
    empates += 1
if ventas_telefono == maximo:
    empates += 1

if empates > 1:
    print("Empate")
elif ventas_tienda == maximo:
    print("Tienda")
elif ventas_web == maximo:
    print("Web")
else:
    print("Teléfono")