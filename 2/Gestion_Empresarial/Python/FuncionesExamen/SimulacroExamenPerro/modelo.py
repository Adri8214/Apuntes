"""UD1 · PT1 · CanAlerta. Solución de las clases."""
import math


class Perro:
    def __init__(self, codigo, propietario, raza, recompensa, estado="PERDIDO"):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código no puede estar vacío")
        if not isinstance(propietario, str) or not propietario.strip():
            raise ValueError("El propietario no puede estar vacío")
        if not isinstance(raza, str) or not raza.strip():
            raise ValueError("La raza no puede estar vacía")

        try:
            recompensa = float(recompensa)
        except (TypeError, ValueError):
            raise ValueError("La recompensa debe ser numérica") from None

        if not math.isfinite(recompensa) or recompensa <= 0:
            raise ValueError("La recompensa debe ser mayor que cero y finita")
        if not isinstance(estado, str) or estado.strip().upper() not in ("PERDIDO", "ENCONTRADO"):
            raise ValueError("Estado no válido")

        self.codigo = codigo.strip().upper()
        self.propietario = propietario.strip()
        self.raza = raza.strip()
        self.recompensa = recompensa
        self.estado = estado.strip().upper()


class RegistroPerdidos:
    def __init__(self):
        self.perros = {}

    def registrar(self, perro):
        """Devuelve True si el perro se incorpora; False si ya existía."""
        codigo = perro.codigo
        if codigo in self.perros:
            return False
        self.perros[codigo] = perro
        return True

    def listar(self):
        """Devuelve todos los objetos Perro del registro."""
        return list(self.perros.values())

    def encontrar(self, codigo):
        """Cambia PERDIDO a ENCONTRADO; False si no puede hacerse."""
        codigo = codigo.strip().upper()
        perro = self.perros.get(codigo)
        if perro is None or perro.estado != "PERDIDO":
            return False
        perro.estado = "ENCONTRADO"
        return True

    def buscar(self, texto):
        """Busca texto en el propietario o la raza, sin distinguir mayúsculas."""
        texto = texto.strip().casefold()
        if not texto:
            return []
        resultados = []
        for perro in self.perros.values():
            if (texto in perro.propietario.casefold()
                    or texto in perro.raza.casefold()):
                resultados.append(perro)
        return resultados

    def resumen(self):
        """Devuelve las cantidades y la recompensa pendiente de los perdidos."""
        perdidos = 0
        encontrados = 0
        recompensa_pendiente = 0.0

        for perro in self.perros.values():
            if perro.estado == "PERDIDO":
                perdidos += 1
                recompensa_pendiente += perro.recompensa
            elif perro.estado == "ENCONTRADO":
                encontrados += 1

        return {
            "total": len(self.perros),
            "perdidos": perdidos,
            "encontrados": encontrados,
            "recompensa_pendiente": recompensa_pendiente,
        }