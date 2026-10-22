"""UD1 · PT1 · PatitasAdopta. Solución de persistencia CSV."""
import csv

from modelos import Perro

CAMPOS = ["codigo", "nombre", "raza", "edad", "peso", "estado"]


def cargar_perros(ruta):
    """Lee perros del CSV convirtiendo edad (int) y peso (float)."""
    perros = []
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != CAMPOS:
            raise ValueError("Las columnas del CSV no tienen el formato esperado")

        for fila in lector:
            perros.append(Perro(
                fila["codigo"],
                fila["nombre"],
                fila["raza"],
                fila["edad"],
                fila["peso"],
                fila["estado"],
            ))

    return perros


def guardar_perros(ruta, perros):
    """Escribe cabeceras y perros en el CSV; devuelve True al terminar."""
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        for perro in perros:
            escritor.writerow({
                "codigo": perro.codigo,
                "nombre": perro.nombre,
                "raza": perro.raza,
                "edad": perro.edad,
                "peso": perro.peso,
                "estado": perro.estado,
            })
    return True