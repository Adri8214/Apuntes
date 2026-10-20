import csv
from pathlib import Path
from modelos import Participante, Taller, Inscripcion

RUTA_PARTICIPANTES = Path("participantes.csv")
RUTA_TALLERES = Path("talleres.csv")
RUTA_INSCRIPCIONES = Path("inscripciones.csv")

def guardar_datos(centro):
    # Guardar participantes
    with open(RUTA_PARTICIPANTES, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["email", "nombre"])
        writer.writeheader()
        for p in centro.participantes.values():
            writer.writerow(p.to_dict())

    # Guardar talleres
    with open(RUTA_TALLERES, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["codigo", "titulo", "plazas"])
        writer.writeheader()
        for t in centro.talleres.values():
            writer.writerow(t.to_dict())

    # Guardar inscripciones
    with open(RUTA_INSCRIPCIONES, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["email_participante", "codigo_taller"])
        writer.writeheader()
        for ins in centro.inscripciones:
            writer.writerow(ins.to_dict())

def cargar_datos(centro):
    # 1. Cargar talleres
    if RUTA_TALLERES.exists():
        with open(RUTA_TALLERES, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                t = Taller(row["codigo"], row["titulo"], int(row["plazas"]))
                centro.talleres[t.codigo] = t

    # 2. Cargar participantes
    if RUTA_PARTICIPANTES.exists():
        with open(RUTA_PARTICIPANTES, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Participante(row["email"], row["nombre"])
                centro.participantes[p.email] = p

    # 3. Cargar inscripciones (validando que existan participante y taller para evitar inconsistencias)[cite: 5]
    if RUTA_INSCRIPCIONES.exists():
        with open(RUTA_INSCRIPCIONES, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                email = row["email_participante"].strip().lower()
                codigo = row["codigo_taller"].strip()
                if email in centro.participantes and codigo in centro.talleres:
                    # Evitar duplicados durante la carga
                    duplicada = any(i.email_participante == email and i.codigo_taller == codigo for i in centro.inscripciones)
                    if not duplicada:
                        centro.inscripciones.append(Inscripcion(email, codigo))