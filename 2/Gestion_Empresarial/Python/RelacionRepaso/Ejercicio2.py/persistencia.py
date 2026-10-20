import csv
from pathlib import Path
from modelos import Carta

RUTA_CARTAS = Path("cartas.csv")

def guardar_coleccion(cartas_dict):
    with open(RUTA_CARTAS, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["codigo", "nombre", "tipo", "rareza", "valor"])
        writer.writeheader()
        for carta in cartas_dict.values():
            writer.writerow(carta.to_dict())

def cargar_coleccion():
    cartas = {}
    if RUTA_CARTAS.exists():
        with open(RUTA_CARTAS, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                c = Carta(
                    row["codigo"],
                    row["nombre"],
                    row["tipo"],
                    row["rareza"],
                    row["valor"]
                )
                cartas[c.codigo] = c
    return cartas