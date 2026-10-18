total_pedido = float(input("Introduce el precio del pedido: "))
premium = input("¿Es premium? (S/N)").strip().upper()

if(total_pedido > 500 or (total_pedido > 250 and premium == "S")):
    print("El cliente es prioritario")
else:
    print("Es un cliente normal")