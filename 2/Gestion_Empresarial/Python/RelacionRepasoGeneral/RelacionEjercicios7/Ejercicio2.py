lista = [5, 10, 15, 20, 25]

for indice, numeros in enumerate(lista, start=1):
    print(f"Posicion {indice}: {numeros}")

suma = sum(lista)
minimo = min(lista)
maximo = max(lista)
media = suma / len(lista)
print(f"Suma: {suma}\nMinimo: {minimo}\nMaximo: {maximo}\nMedia: {media}")