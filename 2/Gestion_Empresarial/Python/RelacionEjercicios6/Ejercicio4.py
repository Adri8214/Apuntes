opcion = -1

while opcion != 0:
    opcion = int(input("Introduce una opción: " \
    "\n1.Alta Ficticia" \
    "\n2.Consulta ficticia" \
    "\n3.Informe ficticio" \
    "\n0.Salir"))

    if opcion == 1:
        print("El alta se ha creado correctamente")
    elif opcion == 2:
        print("La consulta se ha creado correctamente")
    elif opcion == 3:
        print("El informe se ha creado correctamente")
    else:
        print("El programa ha finalizado")