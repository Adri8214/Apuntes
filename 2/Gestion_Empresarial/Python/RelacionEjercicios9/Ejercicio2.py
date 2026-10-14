def leer_entero(mensaje, minimo, maximo):
   
    numero_valido = False
   
    while not numero_valido:
        try:
            numero = int(input(mensaje))
            numero_valido = numero >= minimo and numero <= maximo
            if not numero_valido:
                print("El número debe de estar comprendido entre 1 y 100")
            
        except ValueError:
            print("Introduce un número válido")

    return numero
print(leer_entero("Introduce un número del 1 al 100: ", 1, 100))