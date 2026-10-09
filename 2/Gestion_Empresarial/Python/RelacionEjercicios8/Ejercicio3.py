def aplicar_descuento(importe, porcentaje):
    descuento = (importe * porcentaje) / 100;
    return importe - descuento

importe = (float(input("Seleccione el importe: ")))
porcentaje = (int(input("Seleccione el porcentaje: ")))

print(aplicar_descuento(importe, porcentaje))