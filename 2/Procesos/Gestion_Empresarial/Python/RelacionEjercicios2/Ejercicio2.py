nombrecliente = input("Introduce el nombre del cliente: ")
nombreServicio = input("Introduce el nombre del servicio: ")
precio = float (input("Introduce el precio: "))
cantidad = int (input("Introduce la cantidad: "))

subtotal = precio * cantidad

print(f"Subtotal: {subtotal:.2f}\nNombre cliente: {nombrecliente}\nServicio: {nombreServicio}\nPrecio: {precio}\nCantidad: {cantidad}")