def pedir_datos():
    cliente = input("Cliente: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    descuento = float(input("Descuento: "))
    return cliente, precio, cantidad, descuento


def calcular_total(precio, cantidad, descuento):
    subtotal = precio * cantidad
    return subtotal - subtotal * descuento / 100

def mostrar_resumen(cliente, precio, cantidad, descuento, total):
    print(
        f"Cliente: {cliente}\n"
        f"Precio: {precio:.2f}\n"
        f"Cantidad: {cantidad}\n"
        f"Descuento: {descuento:.2f}%\n"
        f"Total: {total:.2f}\n"
    )

def main():
    cliente, precio, cantidad, descuento = pedir_datos()
    total = calcular_total(precio, cantidad, descuento)
    mostrar_resumen(cliente, precio, cantidad, descuento, total)


main()

