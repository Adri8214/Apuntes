import csv
from pathlib import Path

ruta = Path(__file__).with_name("productos.csv")
productos = [
    {"nombre": "Boligrafo", "precio": 2.5, "cantidad": 90},
    {"nombre": "Cuaderno", "precio": 3.7, "cantidad": 50},
    {"nombre": "Lapiz", "precio": 1.3, "cantidad": 200}
]

with open(ruta, "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio", "cantidad"])
    escritor.writeheader()
    escritor.writerows(productos)
    
with open(ruta, "r", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(f"Nombre: {fila['nombre']}, Precio: {fila['precio']}, Cantidad: {fila['cantidad']}\n")