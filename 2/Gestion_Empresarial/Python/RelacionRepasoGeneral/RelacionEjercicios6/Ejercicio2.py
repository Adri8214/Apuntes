ventas = float(input("Introduce el número de ventas: "))

for numero in range(1,8):
    subtotal = numero * ventas
    media = subtotal / numero
print(f"Ventas: {ventas:.2f}\nSubtotal: {subtotal:.2f}\nMedia: {media:.2f}")