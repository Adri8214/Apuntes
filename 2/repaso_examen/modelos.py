class Bicicleta:
    def __init__(self, codigo, propietario, modelo, valor, estado="ROBADA"):
        self.codigo = codigo
        self.propietario = propietario
        self.modelo = modelo
        self.valor = valor
        self.estado = estado

    def ficha(self):
        return (
            f"{self.codigo} | {self.propietario} | {self.modelo} | "
            f"{self.valor:.2f} EUR | {self.estado}"
        )


class RegistroRobos:
    def __init__(self):
        self.bicicletas = {}

    def registrar(self, bicicleta):
        """Añade una bicicleta si el código no existe."""
        if bicicleta.codigo in self.bicicletas:
            return False

        self.bicicletas[bicicleta.codigo] = bicicleta
        return True

    def listar(self):
        """Devuelve todas las bicicletas."""
        return list(self.bicicletas.values())

    def recuperar(self, codigo):
        """Cambia el estado de ROBADA a RECUPERADA."""
        if codigo not in self.bicicletas:
            return False

        bicicleta = self.bicicletas[codigo]

        if bicicleta.estado == "RECUPERADA":
            return False

        bicicleta.estado = "RECUPERADA"
        return True

    def buscar(self, texto):
        """Busca por propietario o modelo, sin distinguir mayúsculas."""
        resultados = []

        texto = texto.lower()

        for bicicleta in self.bicicletas.values():
            if (
                texto in bicicleta.propietario.lower()
                or texto in bicicleta.modelo.lower()
            ):
                resultados.append(bicicleta)

        return resultados

    def resumen(self):
        """Calcula el resumen de las bicicletas."""
        total = len(self.bicicletas)
        robadas = 0
        recuperadas = 0
        valor_pendiente = 0

        for bicicleta in self.bicicletas.values():
            if bicicleta.estado == "ROBADA":
                robadas += 1
                valor_pendiente += bicicleta.valor
            else:
                recuperadas += 1

        return {
            "total": total,
            "robadas": robadas,
            "recuperadas": recuperadas,
            "valor_pendiente": valor_pendiente
        }