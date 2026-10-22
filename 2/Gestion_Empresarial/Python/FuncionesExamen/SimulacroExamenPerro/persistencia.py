"""UD1 · PT1 · CanAlerta. Solución de persistencia CSV."""
import csv

from modelo import Perro

CAMPOS = ["codigo", "propietario", "raza", "recompensa", "estado"]


def cargar_perros(ruta):
    """Lee perros del CSV, con su recompensa numérica y su estado."""
    perros = []
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != CAMPOS:
            raise ValueError("Las columnas del CSV no tienen el formato esperado")

        for fila in lector:
            perro = Perro(
                fila["codigo"],
                fila["propietario"],
                fila["raza"],
                fila["recompensa"],
                fila["estado"],
            )
            perros.append(perro)

    return perros


def guardar_perros(ruta, perros):
    """Escribe cabeceras y perros en el CSV; devuelve True al terminar."""
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        for perro in perros:
            escritor.writerow({
                "codigo": perro.codigo,
                "propietario": perro.propietario,
                "raza": perro.raza,
                "recompensa": perro.recompensa,
                "estado": perro.estado,
            })
    return True