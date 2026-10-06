nombre_producto = input("Introduce el nombre del producto: ")
precio = int (input("Introduce el precio del producto: "))
cantidad = int (input("Introduce la cantidad: "))
porcentaje_descuento = int (input("Introduce el porcentaje de descuento: "))

subtotal = precio * cantidad
descuento = subtotal * porcentaje_descuento / 100
total = subtotal - descuento

print(f"Nombre: {nombre_producto}\nPrecio: {precio:.2f}\nCantidad: {cantidad:.2f}\nPorcentaje de descuento: {porcentaje_descuento}\nSubtotal: {subtotal:.2f}\nDescuento: {descuento:.2f}\nTotal: {total:.2f}")
