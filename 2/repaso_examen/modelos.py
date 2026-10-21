"""UD1 · PT1 · BiciAlerta. Solución de las clases."""
import math


class Bicicleta:
    def __init__(self, codigo, propietario, modelo, valor, estado="ROBADA"):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código no puede estar vacío")
        if not isinstance(propietario, str) or not propietario.strip():
            raise ValueError("El propietario no puede estar vacío")
        if not isinstance(modelo, str) or not modelo.strip():
            raise ValueError("El modelo no puede estar vacío")

        try:
            valor = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El valor debe ser numérico") from None

        if not math.isfinite(valor) or valor <= 0:
            raise ValueError("El valor debe ser mayor que cero y finito")
        if not isinstance(estado, str) or estado.strip().upper() not in ("ROBADA", "RECUPERADA"):
            raise ValueError("Estado no válido")

        self.codigo = codigo.strip().upper()
        self.propietario = propietario.strip()
        self.modelo = modelo.strip()
        self.valor = valor
        self.estado = estado.strip().upper()


class RegistroRobos:
    def __init__(self):
        self.bicicletas = {}

    def registrar(self, bicicleta):
        """Devuelve True si la bicicleta se incorpora; False si ya existía."""
        codigo = bicicleta.codigo
        if codigo in self.bicicletas:
            return False
        self.bicicletas[codigo] = bicicleta
        return True

    def listar(self):
        """Devuelve todos los objetos Bicicleta del registro."""
        return list(self.bicicletas.values())

    def recuperar(self, codigo):
        """Cambia ROBADA a RECUPERADA; False si no puede hacerse."""
        codigo = codigo.strip().upper()
        bicicleta = self.bicicletas.get(codigo)
        if bicicleta is None or bicicleta.estado != "ROBADA":
            return False
        bicicleta.estado = "RECUPERADA"
        return True

    def buscar(self, texto):
        """Busca texto en el propietario o el modelo, sin distinguir mayúsculas."""
        texto = texto.strip().casefold()
        if not texto:
            return []
        resultados = []
        for bicicleta in self.bicicletas.values():
            if (texto in bicicleta.propietario.casefold()
                    or texto in bicicleta.modelo.casefold()):
                resultados.append(bicicleta)
        return resultados

    def resumen(self):
        """Devuelve las cantidades y el valor pendiente de las robadas."""
        robadas = 0
        recuperadas = 0
        valor_pendiente = 0.0

        for bicicleta in self.bicicletas.values():
            if bicicleta.estado == "ROBADA":
                robadas += 1
                valor_pendiente += bicicleta.valor
            elif bicicleta.estado == "RECUPERADA":
                recuperadas += 1

        return {
            "total": len(self.bicicletas),
            "robadas": robadas,
            "recuperadas": recuperadas,
            "valor_pendiente": valor_pendiente,
        }