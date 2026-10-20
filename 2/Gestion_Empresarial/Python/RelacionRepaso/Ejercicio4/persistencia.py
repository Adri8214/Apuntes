import csv
from pathlib import Path
from modelos import Reparacion, AsistenciaRemota

RUTA_TRABAJOS = Path("trabajos.csv")

def guardar_trabajos(trabajos_dict):
    with open(RUTA_TRABAJOS, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["tipo", "codigo", "cliente", "horas", "precio_pieza", "estado"])
        writer.writeheader()
        for t in trabajos_dict.values():
            tipo = "reparacion" if isinstance(t, Reparacion) else "remota"
            precio_pieza = getattr(t, "precio_pieza", 0.0)
            writer.writerow({
                "tipo": tipo,
                "codigo": t.codigo,
                "cliente": t.cliente,
                "horas": t.horas,
                "precio_pieza": precio_pieza,
                "estado": t.estado
            })

def cargar_trabajos():
    trabajos = {}
    if RUTA_TRABAJOS.exists():
        with open(RUTA_TRABAJOS, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                tipo = row["tipo"].strip().lower()
                codigo = row["codigo"]
                cliente = row["cliente"]
                horas = float(row["horas"])
                estado = row["estado"]
                
                # Reconstruir el subtipo correcto utilizando el campo tipo[cite: 6]
                if tipo == "reparacion":
                    precio_pieza = float(row["precio_pieza"] or 0.0)
                    trabajos[codigo] = Reparacion(codigo, cliente, horas, precio_pieza, estado)
                elif tipo == "remota":
                    trabajos[codigo] = AsistenciaRemota(codigo, cliente, horas, estado)
    return trabajos