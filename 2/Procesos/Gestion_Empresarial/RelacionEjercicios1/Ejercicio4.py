subtotal = 250
descuento = 12

importeDescuento = subtotal * descuento / 100
total = subtotal - importeDescuento

print(f"Descuento: {importeDescuento:.2f}EUR; total: {total:.2f} EUR.")