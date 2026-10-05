nombreProducto = input("Introduce el nombre del producto: ")
precio = int (input("Introduce el precio del producto: "))
cantidad = int (input("Introduce la cantidad: "))
porcentajeDescuento = int (input("Introduce el porcentaje de descuento: "))

subtotal = precio * cantidad
descuento = subtotal * porcentajeDescuento / 100
total = subtotal - descuento

print(f"Nombre: {nombreProducto}\nPrecio: {precio:.2f}\nCantidad: {cantidad:.2f}\nPorcentaje de descuento: {porcentajeDescuento}\nSubtotal: {subtotal:.2f}\nDescuento: {descuento:.2f}\nTotal: {total:.2f}")
