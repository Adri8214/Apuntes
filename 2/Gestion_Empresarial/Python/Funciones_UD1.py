def mostrar_menu():
    menu = (
        "\n--- MENÚ PRINCIPAL ---\n"
        "1. Añadir producto\n"
        "2. Mostrar productos\n"
        "3. Eliminar producto\n"
        "0. Salir\n"
    )
    return menu

def mostrar_menu_y_leer_opcion(menu):
    print(menu)
    opcion = leer_entero("Opción: ")
    return opcion

def bucar_producto (lista) :
    nombre_buscar = input("Dime el nombre del producto que quieres buscar: ")
    for producto in lista : 
        if producto['nombre'] == nombre_buscar :
            print(f"Encontrado: {producto['nombre']} - {producto['stock']} uds")

def modificar_stock (lista) :
    nombre_buscar = input("Nombre del producto que quieres actualizar: ")
    try :
        for producto in lista :
            if producto['nombre'] == nombre_buscar:
                nuevo_stock = int(input("Nuevo stock: "))
                producto['stock'] = nuevo_stock
    except ValueError:
        print("Error: Debes introducir un número")

def mostrar_inventario (lista) :
    for producto in lista :
        print(f"-{producto ['nombre']}: {producto['stock']} uds")


def aniadir_producto (lista) :
    nombre_producto = input("Nombre del producto: ")
    try :
        stock = int(input("Stock del producto: "))
        lista.append({"nombre": nombre_producto, "stock": stock})
    except ValueError :
        print("Error: debes introducir un número")

def guardar_csv (lista) :
    with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo :
        campos = ["nombre", "stock"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(lista)
    print("Datos guardados en inventario.csv")

def pedir_datos():
    cliente = input("Cliente: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    descuento = float(input("Descuento: "))
    return cliente, precio, cantidad, descuento

def calcular_total(precio, cantidad, descuento):
    subtotal = cantidad * precio
    return subtotal - (subtotal * descuento / 100)

def mostrar_resumen(cliente, precio, cantidad, descuento, total):
    print(
        f"Cliente: {cliente}",
        f"Precio: {precio:.2f}",
        f"Cantidad: {cantidad}",
        f"Descuento: {descuento:.2f}",
        f"Total: {total:.2f}"
    )

def aplicar_descuento(importe, porcentaje=0):
    return importe - importe * porcentaje / 100

def leer_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            return None


numero = leer_entero("Introduce un número entero: ")

if numero is None:
    print("Error: debes introducir un número entero.")
else:
    print(f"Número introducido: {numero}")