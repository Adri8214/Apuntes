existenciasIniciales = int(input("Introduce el numero de existencias iniciales: "))
unidadesRecibidas = int(input("Introduce el número de unidades recibidas: "))
unidadesVendidas = int(input("Introduce el número de unidades vendidas: "))

stockFinal = (existenciasIniciales + unidadesRecibidas) - unidadesVendidas

print(f"Unidades iniciales: {existenciasIniciales}\nUnidades recibidas: {unidadesRecibidas}\nUnidades vendidas: {unidadesRecibidas}\nUnidades restantes: {stockFinal}")