class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Comercial(Empleado):
    def __init__(self, nombre, salario, ventas):
        super().__init__(nombre, salario)
        self.ventas = ventas

    def calcular_bonus(self):
        if self.ventas <= 0:
            return False
        else:
            return self.ventas * 0.05

    def resumen(self):
        return f"Nombre: {self.nombre} | Salario: {self.salario} | Ventas: {self.ventas} | Bonus: {self.calcular_bonus()}"

empleado1 = Empleado("Luis", 2000)
comercial1 = Comercial("Manuel", 3000, 5780)

print(comercial1.resumen())