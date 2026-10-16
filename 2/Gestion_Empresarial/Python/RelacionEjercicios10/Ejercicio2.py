class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def vender(self, cantidad):
        if cantidad <= 0 or cantidad > self.stock:
            return False
        
        self.stock -= cantidad
        return True

    def reponer(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad


producto = Producto("Boligrafo", 2.5, 100)
print(f"Stock inicial: {producto.stock}")
producto.vender(2)
producto.reponer(30)
print(f"Stock actual: {producto.stock}")
