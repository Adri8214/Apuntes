productos = ["Teclado", "Ratón", "Monitor"]
productos.append("Webcam")
productos.remove("Ratón")
productos.sort()

lineas = []

for numero, productos in enumerate(productos, start=1):
    lineas.append(f"{numero}. {productos}")

print("\n".join(lineas)) 