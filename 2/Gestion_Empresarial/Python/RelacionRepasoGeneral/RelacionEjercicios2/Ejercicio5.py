cliente = input("Introduce el nombre del cliente: ")

producto1 = input("Introduce el nombre del primer prodcuto: ")
precio1 = float(input("Introduce el precio del primer producto: "))
cantidad1 = int(input("Introduce la cantidad del primer prodcuto"))

subtotal1 = precio1 * cantidad1

producto2 = input("Introduce el nombre del primer prodcuto: ")
precio2 = float(input("Introduce el precio del primer producto: "))
cantidad2 = int(input("Introduce la cantidad del primer prodcuto"))

subtotal2 = precio2 * cantidad2

precio_total = subtotal1 + subtotal2

print("=== RESUMEN ===")
print(f"Nombre del cliente: {cliente}\n")
print(f"Nombre del primer producto: {producto1}")
print(f"Precio del primer prodcuto: {precio1}")
print(f"Cantidad del primer prodcuto: {cantidad1}")
print(f"Subtotal: {subtotal1:.2f}")

print(f"Nombre del segundo producto: {producto2}")
print(f"Precio del segundo prodcuto: {precio2}")
print(f"Cantidad del segundo prodcuto: {cantidad2}")
print(f"Subtotal: {subtotal2:.2f}")

print(f"Total: {precio_total:.2f} EUR")