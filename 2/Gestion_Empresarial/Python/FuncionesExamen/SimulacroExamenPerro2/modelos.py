"""UD1 · PT1 · PatitasAdopta. Solución de las clases."""
import math


class Perro:
    def __init__(self, codigo, nombre, raza, edad, peso, estado="DISPONIBLE"):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código no puede estar vacío")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not isinstance(raza, str) or not raza.strip():
            raise ValueError("La raza no puede estar vacía")

        if isinstance(edad, bool):
            raise ValueError("La edad debe ser un entero")
        try:
            edad = int(edad)
        except (TypeError, ValueError):
            raise ValueError("La edad debe ser un entero") from None
        if not 0 <= edad <= 30:
            raise ValueError("La edad debe estar entre 0 y 30 años")

        try:
            peso = float(peso)
        except (TypeError, ValueError):
            raise ValueError("El peso debe ser numérico") from None
        if not math.isfinite(peso) or peso <= 0:
            raise ValueError("El peso debe ser mayor que cero y finito")

        if not isinstance(estado, str) or estado.strip().upper() not in ("DISPONIBLE", "ADOPTADO"):
            raise ValueError("Estado no válido")

        self.codigo = codigo.strip().upper()
        self.nombre = nombre.strip()
        self.raza = raza.strip()
        self.edad = edad
        self.peso = peso
        self.estado = estado.strip().upper()


class Protectora:
    def __init__(self):
        self.perros = {}

    def registrar(self, perro):
        """Devuelve True si el perro ingresa; False si el código ya existía."""
        if perro.codigo in self.perros:
            return False
        self.perros[perro.codigo] = perro
        return True

    def listar(self):
        """Devuelve todos los objetos Perro de la protectora."""
        return list(self.perros.values())

    def adoptar(self, codigo):
        """Cambia DISPONIBLE a ADOPTADO; False si no puede hacerse."""
        perro = self.perros.get(codigo.strip().upper())
        if perro is None or perro.estado != "DISPONIBLE":
            return False
        perro.estado = "ADOPTADO"
        return True

    def dar_de_baja(self, codigo):
        """True si el perro existía y se ha eliminado del registro."""
        return self.perros.pop(codigo.strip().upper(), None) is not None

    def disponibles_por_edad(self):
        """Perros DISPONIBLES ordenados de menor a mayor edad (y por nombre)."""
        disponibles = [p for p in self.perros.values() if p.estado == "DISPONIBLE"]
        return sorted(disponibles, key=lambda p: (p.edad, p.nombre.casefold()))

    def estadisticas(self):
        """Cantidades, peso medio de los disponibles y perro más pesado."""
        disponibles = 0
        adoptados = 0
        suma_peso = 0.0
        mas_pesado = None

        for perro in self.perros.values():
            if perro.estado == "DISPONIBLE":
                disponibles += 1
                suma_peso += perro.peso
            elif perro.estado == "ADOPTADO":
                adoptados += 1
            if mas_pesado is None or perro.peso > mas_pesado.peso:
                mas_pesado = perro

        peso_medio = suma_peso / disponibles if disponibles else 0.0

        return {
            "total": len(self.perros),
            "disponibles": disponibles,
            "adoptados": adoptados,
            "peso_medio_disponibles": peso_medio,
            "mas_pesado": mas_pesado,
        }