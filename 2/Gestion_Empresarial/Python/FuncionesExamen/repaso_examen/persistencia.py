"""UD1 · PT1 · BiciAlerta. Solución de persistencia CSV."""
import csv

from modelos import Bicicleta

CAMPOS = ["codigo", "propietario", "modelo", "valor", "estado"]


def cargar_bicicletas(ruta):
    """Lee bicicletas del CSV, con su valor numérico y su estado."""
    bicicletas = []
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != CAMPOS:
            raise ValueError("Las columnas del CSV no tienen el formato esperado")

        for fila in lector:
            bicicleta = Bicicleta(
                fila["codigo"],
                fila["propietario"],
                fila["modelo"],
                fila["valor"],
                fila["estado"],
            )
            bicicletas.append(bicicleta)

    return bicicletas


def guardar_bicicletas(ruta, bicicletas):
    """Escribe cabeceras y bicicletas en el CSV; devuelve True al terminar."""
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        for bicicleta in bicicletas:
            escritor.writerow({
                "codigo": bicicleta.codigo,
                "propietario": bicicleta.propietario,
                "modelo": bicicleta.modelo,
                "valor": bicicleta.valor,
                "estado": bicicleta.estado,
            })
    return True