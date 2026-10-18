destino = input("Destino: (PENINSULA - BALEARES - CANARIAS): ").strip().upper()
total_pedido = float(input("Total pedido: "))

if destino == "PENINSULA": 
    if total_pedido >= 100:
        print("Envio gratuito")
    else:
        subtotal = total_pedido * 6
        print(subtotal)
elif destino == "BALEARES":
    subtotal = total_pedido * 12
    print(subtotal)
elif destino == "CANARIAS": 
    subtotal = total_pedido * 18
    print(subtotal)
else:
    print("Introduce un destino valido")
