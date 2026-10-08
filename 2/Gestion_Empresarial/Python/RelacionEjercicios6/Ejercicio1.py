num_pedidos = int(input("Introduce el número de pedidos "))

if num_pedidos >= 0:
    codigos = []
    for numero in range(1, num_pedidos + 1):
        codigos.append(f"PED-{numero:03d}")
    print("\n".join(codigos))
else:
    print("El número de pedidos debe de ser positivo")