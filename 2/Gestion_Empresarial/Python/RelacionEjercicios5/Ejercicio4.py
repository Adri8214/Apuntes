destino = input("Introduce el destino: (PENINSULA, BALEARES, CANARIAS): ").strip().upper()
total_pedido = int(input("Introduce el total del pedido: "))

if destino == "PENINSULA":
    if total_pedido >= 100:
        gastos_envio = 0
    else:
            gastos_envio = 6
    subtotal = total_pedido + gastos_envio
    print(f"Gastos de envío: {gastos_envio:.2f} EUR\nSubtotal: {subtotal:.2f}")
elif destino == "BALEARES":
    gastos_envio = 12
    subtotal = total_pedido + gastos_envio
    print(f"Gastos de envío: {gastos_envio:.2f} EUR\nSubtotal: {subtotal:.2f}")
    
elif destino == "CANARIAS":
    gastos_envio = 18
    subtotal = total_pedido + gastos_envio
    print(f"Gastos de envío: {gastos_envio:.2f} EUR\nSubtotal: {subtotal:.2f}")

else:
    print("El destino no es válido")
