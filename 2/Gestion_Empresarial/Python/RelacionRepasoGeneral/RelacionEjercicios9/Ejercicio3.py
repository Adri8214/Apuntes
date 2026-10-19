from pathlib import Path

ruta = Path(__file__).with_name("clientes.txt")
clientes = []

for numero in range(1,4):
    nombre = input(f"Nombre del cliente {numero}: ").strip()
    ciudad = input(f"Nombre de la ciudad {numero}: ").strip()
    clientes.append(f"{nombre};{ciudad}")

with open(ruta, "w", encoding="utf-8") as archivo:
    for cliente in clientes:
        archivo.write(cliente + "\n")

print("\nContenido de clientes.txt: ")
with open(ruta, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.rstrip("\n"))