with open("clientes.txt", "w", encoding="utf-8") as archivo:
    cliente_max = 4
    cliente_min = 1
    for i in range(cliente_min,cliente_max):
        
        print(f"Cliente: {i}.")
        nombre = (input(f"Introduce el nombre del cliente: "))
        ciudad = (input(f"Introduce la ciudad del cliente: "))

        archivo.write(f"{nombre};{ciudad}\n")
        
with open("clientes.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())        
