class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        
class Comercial(Empleado):
    def __init__(self, nombre, salario, ventas):
        super().__init__(nombre, salario)
        self.ventas = ventas
    
    def calcular_bonus(self):
        return self.ventas * 0.5
    
    def resumen(self):
        return (
            f"Comercial: {self.nombre}\n"
            f"Salario: {self.salario:.2f} EUR\n"
            f"Ventas: {self.ventas:.2f} EUR\n"
            f"Bonus (5%): {self.calcular_bonus():.2f}"
        )
comercial = Comercial("Ramon", 2000, 2345)
print(comercial.resumen())
        