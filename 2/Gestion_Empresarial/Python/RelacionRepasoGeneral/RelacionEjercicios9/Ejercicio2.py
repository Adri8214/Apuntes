def leer_entero(mensaje, minimo, maximo):
    numero =  minimo - 1

    while numero < minimo or numero > maximo:
        try:
            numero = int(input(mensaje))
            if numero <= minimo or numero > maximo:
                print(f"Introduce un número entre {minimo} y {maximo}")

        except ValueError:
            print("Debes de introducir un número entero")

    return numero

cantidad = leer_entero("Cantidad (1-100): ", 1,100)
print(f"Cantidad válida: {cantidad}")