import csv
from pathlib import Path

ruta = Path(__file__).with_name("productos.csv")
productos = [
    {"nombre": "Teclado", "precio": 24, "stock": 90},
    {"nombre": "Raton", "precio": 35, "stock": 240},
    {"nombre": "Monitor", "precio": 12, "stock": 16}
]

with open(ruta, "w", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio", "stock"])
    escritor.writeheader()
    escritor.writerows(productos)

print("Contenido de productos: ")
with open(ruta, "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(f"{fila['nombre']}: {fila['precio']} EUR, stock {fila['stock']}")