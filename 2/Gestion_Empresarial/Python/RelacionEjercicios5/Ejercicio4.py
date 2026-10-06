destino = input("Introduce el destino: PENINSULA, BALEARES, CANARIAS")
total_pedido = int(input("Introduce el total del pedido"))



if destino == "PENINSULA" and total_pedido >= 100:
    print(f"Destino: {destino}\nCoste del pedido: {total_pedido}")  
elif destino == "PENINSULA" and total_pedido < 100:
    total_pedido = total_pedido + 6
    print(f"Destino: {destino}\nCoste del pedido: {total_pedido}")  
elif