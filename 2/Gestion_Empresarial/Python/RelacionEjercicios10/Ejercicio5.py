class LineaPedido:
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
        self.lineas.append(linea)

    def total(self):
        return sum(linea.subtotal() for linea in self.lineas)


pedido = Pedido("María García")
pedido.agregar_linea(LineaPedido("Boligrafo", 2, 30))
pedido.agregar_linea(LineaPedido("Lapiz", 1, 300))
pedido.agregar_linea(LineaPedido("Papel", 2, 350))

print(f"Pedido de {pedido.cliente}:")

for linea in pedido.lineas:
    print(f"{linea.producto}: {linea.cantidad} x {linea.precio:.2f} = {linea.subtotal():.2f} EUR")

print(f"Total: {pedido.total():.2f} EUR")
total_manual = 2 * 30.00 + 1 * 300.00 + 2 * 350
print(f"Coincide con la suma manual: {abs(pedido.total() - total_manual) < 0.001}")