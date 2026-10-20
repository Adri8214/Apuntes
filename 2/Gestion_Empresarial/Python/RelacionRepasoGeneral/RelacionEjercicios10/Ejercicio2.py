class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Stock: {self.stock}")

    def vender_cantidad(self, cantidad):
        if cantidad <= 0:
            return False
        else:
            self.stock -= cantidad
            return True

    def reponer(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad

producto1 = Producto("Monitor",25,200)
producto2 = Producto("Raton",12.5,32)

producto1.vender_cantidad(25)
producto2.reponer(50)

producto1.mostrar()
print("\n")
producto2.mostrar()