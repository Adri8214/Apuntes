subtotal = 250
descuento = 12

calcular_descuento = subtotal * 12 / 100
descuento_aplicado = subtotal - calcular_descuento

print(f"Descuento: {calcular_descuento:.2f} EUR\nTotal: {descuento_aplicado:.2f} EUR")