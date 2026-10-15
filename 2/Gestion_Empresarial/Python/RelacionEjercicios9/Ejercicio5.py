def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal

def aplicar_descuento(importe, porcentaje):
    descuento = importe * porcentaje / 100
    descuento_aplicado = importe - descuento
    return descuento_aplicado

def main():
    print("--- Calculadora de precios y descuentos ---")
    
    precio = float(input("Introduce el precio del producto: "))
    cantidad = int(input("Introduce la cantidad del producto: "))
        
    subtotal = calcular_subtotal(precio, cantidad)
    print(f"El total del producto es de: {subtotal}")
    
    porcentaje = int(input("Introduce el porcentaje: "))
    total_con_descuento = aplicar_descuento(subtotal, porcentaje)
    print(f"El total con descuento es {total_con_descuento} EUR")
    
if __name__ == "__main__":
    main()