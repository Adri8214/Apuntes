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


def anadir_producto(productos):
    nombre_producto = input("Introduce el nombre del producto: ").strip()
    try:
        precio = float(input("Introduce el precio del producto: "))
        stock = int(input("Introduce el stock del producto: "))
        productos.append({"nombre": nombre_producto, "precio": precio, "stock": stock})
        return f"Producto {nombre_producto} añadido"
    except ValueError:
        return "El precio y el stock tienen que ser números"

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


def formatear_producto(numero, producto):
    return (
        f"{numero}. {producto['nombre']} | "
        f"{producto['precio']:.2f} EUR | Stock: {producto['stock']}"
    )

def listar_productos(productos):
    if not productos:
        return "No hay productos"
    else:
        lineas = []
        for numero, producto in enumerate(productos, start=1):
            lineas.append(formatear_producto(numero,producto))
        return "\n".join(lineas)

def convertir_cantidad(texto):
    """Devuelve una cantidad positiva o None si el dato es inválido."""
    try:
        cantidad = int(texto)
    except ValueError:
        return None
    return cantidad if cantidad > 0 else None

def mostrar_pedido(pedido):
    """Devuelve un listado de líneas; la impresión se hace en main()."""
    if not pedido.lineas:
        lineas = ["El pedido está vacío."]
    else:
        lineas = [f"Pedido de {pedido.cliente}:"]
        for linea in pedido.lineas:
            lineas.append(
                f"{linea.producto.nombre} | {linea.cantidad} x "
                f"{linea.producto.precio:.2f} = {linea.subtotal():.2f} EUR"
            )
    lineas.append(f"Total: {pedido.total():.2f} EUR")
    return lineas
