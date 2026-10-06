precio = int(input("Introduce el precio del producto: "))
cantidad = int(input("Introduce la cantidad del producto: "))

subtotal = precio * cantidad
if cantidad < 5:
    descuento = subtotal * 0 / 100    
    total = subtotal - descuento
    print(f"Subtotal: {subtotal}\nDescuento: {descuento}\nTotal: {total}")
    
elif cantidad >= 5 and cantidad <= 9:
    descuento = subtotal * 5 / 100
    total = subtotal - descuento
    print(f"Subtotal: {subtotal}\nDescuento: {descuento}\nTotal: {total}")

else:
    descuento = subtotal * 10 / 100
    total = subtotal - descuento
    print(f"Subtotal: {subtotal}\nDescuento: {descuento}\nTotal: {total}")
    
