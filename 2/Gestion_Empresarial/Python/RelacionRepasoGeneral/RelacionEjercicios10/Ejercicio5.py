class Linea_pedido:
    def __init__(self, producto, precio, cantidad):
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        return self.precio * self.cantidad

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.lineas = []

    def agregar_linea(self, linea):
        return self.lineas.append(linea)

    def total(self):
        return sum(linea.subtotal() for linea in self.lineas)

pedido = Pedido("María García")
pedido.agregar_linea(Linea_pedido("Ratón", 15.00, 2))
pedido.agregar_linea(Linea_pedido("Teclado", 80.00, 1))
pedido.agregar_linea(Linea_pedido("Cable USB", 4.50, 3))

print(f"Pedido de {pedido.cliente}:")
for linea in pedido.lineas:
    print(f"{linea.producto}: {linea.cantidad} x {linea.precio:.2f} = {linea.subtotal():.2f} EUR")

print(f"Total: {pedido.total():.2f} EUR")
total_manual = 2 * 15.00 + 1 * 80.00 + 3 * 4.50
print(f"Coincide con la suma manual: {abs(pedido.total() - total_manual) < 0.001}")