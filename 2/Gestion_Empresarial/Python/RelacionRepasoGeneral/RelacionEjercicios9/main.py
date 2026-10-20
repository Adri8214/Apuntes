from Ejercicio5 import calcular_subtotal, aplicar_descuento

def main():
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    porcentaje = int(input("Porcentaje"))

    subtotal = calcular_subtotal(precio, cantidad)
    total = aplicar_descuento(subtotal, porcentaje)

    print(f"Subtotal: {subtotal:.2f} EUR")
    print(f"Descuento: {porcentaje:.2f} EUR")
    print(f"Total: {total:.2f} EUR")

if __name__ == "__main__":
    main()