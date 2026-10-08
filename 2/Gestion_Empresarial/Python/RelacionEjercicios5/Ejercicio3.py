total_pedido = int(input("Introduce el precio total del pedido: "))
premium = input("¿El cliente es vip? (S/N): ").strip().upper()

if total_pedido > 500 or (premium == "S" and total_pedido > 250):
    print("El pedido es prioritario")
else:
    print("El pedidio no es prioritario")