nombre_producto = input("Nombre producto: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = int(input("Porcentaje de descuento: "))

subtotal = precio * cantidad
descuento_aplicado = subtotal * porcentaje_descuento / 100
precio_total = subtotal - descuento_aplicado

print("=== RESUMEN ===")
print(f"Nombre producto: {nombre_producto}\n")
print(f"Precio: {precio:.2f}")
print(f"Cantidad: {cantidad}")
print(f"Descuento: {porcentaje_descuento}%")
print(f"Subtotal: {subtotal:.2f}")
print(f"Descuento aplicado: {descuento_aplicado:.2f} EUR")
print(f"Precio total: {precio_total:.2f}")