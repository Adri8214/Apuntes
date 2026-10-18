numero_pedidos = int(input("Introduce el número de pedidos que se van a realizar: "))

if numero_pedidos < 1:
        print("El numero de pedidos debe de ser mayor que 1")
else:
    for numero in range(1,numero_pedidos + 1):
        print(f"PED-{numero:03d}")