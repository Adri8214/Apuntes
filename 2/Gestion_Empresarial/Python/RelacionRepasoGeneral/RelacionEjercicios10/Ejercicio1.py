class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Stock: {self.stock}")


producto1 = Producto("Monitor",25,200)
producto2 = Producto("Raton",12.5,32)

producto1.mostrar()
print("\n")
producto2.mostrar()