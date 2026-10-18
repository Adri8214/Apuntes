lista = ["Teclado", "Raton", "Monitor"]
lista.append("Webcam")
lista.remove("Raton")

for indice, listas in enumerate(lista, start=1):
    print(f"Posicion {indice}: {listas}")