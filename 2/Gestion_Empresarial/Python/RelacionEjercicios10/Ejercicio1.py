class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Stock: {self.stock}")
        print("------------------------")
    
producto1 = Producto("Boligrafo", 2.5, 20)
producto2 = Producto("Folio", 0.10, 190)
    
producto1.mostrar()
producto2.mostrar()