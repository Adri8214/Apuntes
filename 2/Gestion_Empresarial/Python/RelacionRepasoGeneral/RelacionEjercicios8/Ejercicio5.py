def pedir_datos():
    cliente = input("Cliente: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    descuento = float(input("Descuento: "))
    return cliente, precio, cantidad, descuento

def calcular_total(precio, cantidad, descuento):
    subtotal = cantidad * precio
    return subtotal - (subtotal * descuento / 100)

def mostrar_resumen(cliente, precio, cantidad, descuento, total):
    print(
        f"Cliente: {cliente}",
        f"Precio: {precio:.2f}",
        f"Cantidad: {cantidad}",
        f"Descuento: {descuento:.2f}",
        f"Total: {total:.2f}"
    )

def main():
    cliente, precio, cantidad, descuento = pedir_datos()
    total = calcular_total(precio, cantidad, descuento)
    mostrar_resumen(cliente, precio, cantidad, descuento, total)

main()