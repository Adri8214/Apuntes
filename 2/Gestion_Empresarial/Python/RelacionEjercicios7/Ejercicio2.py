precios = [10, 20, 30, 40, 50]

linea = []

for numero in precios:
    linea.append(numero)

print (linea)

cantidad_precios = len(precios)
suma = sum(precios)
minimo = min(precios)
maximo = max(precios)
media = suma / cantidad_precios

print(
    f"Cantidad de precios: {cantidad_precios}\n"
    f"Suma: {suma:.2f}\n"
    f"Mínimo: {minimo}\n"
    f"Máximo: {maximo}\n"
    f"Media: {media:.2f}"
)