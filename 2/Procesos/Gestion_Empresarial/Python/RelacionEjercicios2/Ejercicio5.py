nombre_cliente = input("Introduce el nombre del cliente: ")

nombre_producto1 = input("Introduce el nombre del primer producto: ")
precio_producto1 = int(input("Introduce el precio del primer producto: "))
cantidad_producto1 = int(input("Introduce la cantidad del primer producto: "))

nombre_producto2 = input("Introduce el nombre del segundo producto: ")
precio_producto2 = int(input("Introduce el precio del segundo producto: "))
cantidad_producto2 = int(input("Introduce la cantidad del segundo producto: "))

subtotal1 = precio_producto1 * cantidad_producto1
subtotal2 = precio_producto2 * cantidad_producto2

total = subtotal1 + subtotal2

print(f"Nombre del cliente: {nombre_cliente}")

print(f"Nombre del producto 1: {nombre_producto1}\n")
print(f"Precio del producto 1: {precio_producto1}\n")
print(f"Cantidad del producto 1: {cantidad_producto1}\n")

print(f"Nombre del producto 2: {nombre_producto2}\n")
print(f"Precio del producto 2: {precio_producto2}\n")
print(f"Cantidad del producto 2: {cantidad_producto2}\n")
print(f"Con: {cantidad_producto1}\n artículos a {precio_producto1} y {cantidad_producto2} artículos a {precio_producto2} EUR, total {total} EUR")