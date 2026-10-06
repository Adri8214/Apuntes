nombre_cliente = input("Introduce el nombre del cliente: ")
nombre_servicio = input("Introduce el nombre del servicio: ")
precio = float (input("Introduce el precio: "))
cantidad = int (input("Introduce la cantidad: "))

subtotal = precio * cantidad

print(f"Subtotal: {subtotal:.2f}\nNombre cliente: {nombre_cliente}\nServicio: {nombre_servicio}\nPrecio: {precio}\nCantidad: {cantidad}")