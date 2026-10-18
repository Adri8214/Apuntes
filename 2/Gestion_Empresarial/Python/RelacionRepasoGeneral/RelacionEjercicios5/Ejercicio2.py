precio_unitario = float(input("Introduce el precio: "))
cantidad = int(input("Introduce la cantidad: "))

if cantidad < 5:
    subtotal = precio_unitario * cantidad
    print(f"Subtotal: {subtotal:.2f}")
elif cantidad <= 5 and cantidad >= 9:
    subtotal = precio_unitario * cantidad
    descuento = subtotal * 0.5
    total = subtotal - descuento
    print(f"Subtotal: {subtotal}\nPorcentaje aplicado: {descuento}\n Total: {total}")
elif cantidad >= 10:
    subtotal = precio_unitario * cantidad
    descuento = subtotal * 0.10
    total = subtotal - descuento
    print(f"Subtotal: {subtotal}\nPorcentaje aplicado: {descuento}\n Total: {total}")
else:
    print("Introduce cantidades positivas")
