ventas_dinero = int(input("Introduce el dinero producido por las ventas por día: "))

for ventas in range(1,8):
    total = ventas_dinero * ventas
    media = total / 7
print(f"{ventas_dinero} EUR en ventas por día\nTotal: {total:.2f}\nMedia: {media:.2f}")