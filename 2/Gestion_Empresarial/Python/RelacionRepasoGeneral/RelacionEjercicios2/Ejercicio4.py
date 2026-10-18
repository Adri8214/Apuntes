producto = input("Producto: ")
existencias_iniciales = int(input("Existencias iniciales: "))
unidades_recibidas = int(input("Unidades recibidas: "))
unidades_vendidas = int(input("Unidades vendidas: "))

stock_final = (existencias_iniciales + unidades_recibidas) - unidades_vendidas

print("=== RESUMEN ===\n")
print(f"Nombre: {producto}")
print(f"Existencias iniciales: {existencias_iniciales}")
print(f"Unidades recbidas: {unidades_recibidas}")
print(f"Unidades vendidas: {unidades_vendidas}")
print(f"Stock final: {stock_final}")