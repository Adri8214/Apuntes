"""Persistencia de bicicletas en un archivo CSV."""

import csv
from pathlib import Path
from modelos import Bicicleta

CAMPOS = ["codigo", "propietario", "modelo", "valor", "estado"]


def cargar_bicicletas(ruta):
    """Lee el CSV y devuelve una lista de bicicletas."""
    bicicletas = []
    codigos = set()

    with open(ruta, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        if lector.fieldnames != CAMPOS:
            raise ValueError("Las columnas del CSV no son correctas.")

        for fila in lector:
            codigo = fila["codigo"].strip()

            if not codigo:
                raise ValueError("Hay una bicicleta sin código.")

            if codigo in codigos:
                raise ValueError(f"Código duplicado: {codigo}")

            try:
                valor = float(fila["valor"])
            except ValueError:
                raise ValueError("El valor debe ser numérico.") from None

            if valor <= 0 or valor == float("inf") or valor != valor:
                raise ValueError("El valor debe ser positivo y finito.")

            bicicleta = Bicicleta(
                codigo,
                fila["propietario"],
                fila["modelo"],
                valor,
                fila["estado"].strip().upper()
            )

            bicicletas.append(bicicleta)
            codigos.add(codigo)

    return bicicletas


def guardar_bicicletas(ruta, bicicletas):
    """Guarda todas las bicicletas en el CSV."""
    codigos = set()

    for bicicleta in bicicletas:
        if bicicleta.codigo in codigos:
            raise ValueError(f"Código duplicado: {bicicleta.codigo}")

        codigos.add(bicicleta.codigo)

    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()

        for bicicleta in bicicletas:
            escritor.writerow({
                "codigo": bicicleta.codigo,
                "propietario": bicicleta.propietario,
                "modelo": bicicleta.modelo,
                "valor": bicicleta.valor,
                "estado": bicicleta.estado
            })

    return True