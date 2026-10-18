opcion = -1

while opcion != 0:
    print("1)Alta ficticia\n2)Consulta ficticia\n3)Informe ficticio\n0)Salir")
    opcion = int(input("Introduce una opcion (1-3): "))

    if opcion == 1:
        print("Alta realizada con exito")
    elif opcion == 2:
        print("Consulta realizada correctamente")
    elif opcion == 3:
        print("Informe")
    else:
        print("Introduce un número válido") 
    