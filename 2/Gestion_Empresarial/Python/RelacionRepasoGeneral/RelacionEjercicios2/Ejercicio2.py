nombre_producto = input("Nombre producto: ")
nombre_servicio = input("Nombre del servicio: ")
precio_unitario = float(input("Introduce el precio: "))
cantidad = int(input("Introduce la cantidad: "))

subtotal = precio_unitario * cantidad
print("=== RESUMEN ===\n")
print(f"Nombre producto: {nombre_producto}")
print(f"Servicio: {nombre_servicio}")
print(f"Precio unitario: {precio_unitario:.2f}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: {subtotal:.2f} EUR")