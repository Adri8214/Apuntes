import csv
from pathlib import Path
from modelos import Producto, Venta, LineaVenta

RUTA_PRODS = Path("productos.csv")
RUTA_VENTAS = Path("ventas.csv")

def guardar_productos(productos):
    with open(RUTA_PRODS, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["codigo", "nombre", "categoria", "precio", "stock"])
        writer.writeheader()
        for p in productos.values():
            writer.writerow(p.to_dict())

def cargar_productos():
    productos = {}
    if RUTA_PRODS.exists():
        with open(RUTA_PRODS, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Producto(
                    row["codigo"],
                    row["nombre"],
                    row["categoria"],
                    row["precio"],
                    row["stock"]
                )
                productos[p.codigo] = p
    return productos

def guardar_ventas(ventas_cerradas):
    with open(RUTA_VENTAS, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["numero", "cliente", "codigo_producto", "cantidad", "precio_unitario"])
        writer.writeheader()
        for v in ventas_cerradas:
            for l in v.lineas:
                writer.writerow({
                    "numero": v.numero,
                    "cliente": v.cliente,
                    "codigo_producto": l.producto,
                    "cantidad": l.cantidad,
                    "precio_unitario": l.precio_unitario
                })

def cargar_ventas():
    ventas_map = {}
    if RUTA_VENTAS.exists():
        with open(RUTA_VENTAS, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                num = row["numero"]
                if num not in ventas_map:
                    ventas_map[num] = Venta(num, row["cliente"], cerrada=True)
                linea = LineaVenta(row["codigo_producto"], int(row["cantidad"]), float(row["precio_unitario"]))
                ventas_map[num].agregar_linea(linea)
    return list(ventas_map.values())