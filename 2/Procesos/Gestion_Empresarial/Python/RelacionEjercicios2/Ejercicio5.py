nombreCliente = input("Introduce el nombre del cliente: ")

nombreProducto1 = input("Introduce el nombre del primer producto: ")
precioProducto1 = int(input("Introduce el precio del primer producto: "))
cantidadProducto1 = int(input("Introduce la cantidad del primer producto: "))

nombreProducto2 = input("Introduce el nombre del segundo producto: ")
precioProducto2 = int(input("Introduce el precio del segundo producto: "))
cantidadProducto2 = int(input("Introduce la cantidad del segundo producto: "))

subtotal1 = precioProducto1 * cantidadProducto1
subtotal2 = precioProducto2 *cantidadProducto2

total = subtotal1 + subtotal2

print(f"Nombre del cliente: {nombreCliente}")

print(f"Nombre del producto 1: {nombreProducto1}\n")
print(f"Precio del producto 1: {precioProducto1}\n")
print(f"Cantidad del producto 1: {cantidadProducto1}\n")

print(f"Nombre del producto 2: {nombreProducto2}\n")
print(f"Precio del producto 2: {precioProducto2}\n")
print(f"Cantidad del producto 2: {cantidadProducto2}\n")
print(f"Con: {cantidadProducto1}\n artículos a {precioProducto1} y {cantidadProducto2} artículos a {precioProducto2} EUR, total {total} EUR")