import csv
from pathlib import Path

RUTA_CSV = Path(__file__).with_name("inventario.csv")


productos = [
    {"nombre": "Teclado", "precio": 25, "stock": 200},
    {"nombre": "Raton", "precio": 10, "stock": 140}
]

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

def aniadir_producto(productos):
    nombre_producto = input("Introduce el nombre del producto: ").strip()
    try:
        precio = float(input("Introduce el precio del producto: "))
        stock = int(input("Introduce el stock del producto: "))
        productos.append({"nombre": nombre_producto, "precio": precio, "stock": stock})
        return f"Producto {nombre_producto} añadido"
    except ValueError:
        return "El precio y el stock tienen que ser números"

def modificar_stock(productos):
    nombre_buscar = input("Nombre del producto que quieres actualizar: ").strip()

    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            try:
                nuevo_stock = int(input("Nuevo stock: "))

                if nuevo_stock < 0:
                    return "El stock no puede ser negativo"

                producto["stock"] = nuevo_stock
                return "Stock modificado correctamente"

            except ValueError:
                return "Error: Debes introducir un número"

    return "Producto no encontrado"

def buscar_producto (productos) :
    nombre_buscar = input("Dime el nombre del producto que quieres buscar: ")
    for producto in productos : 
        if producto['nombre'].lower() == nombre_buscar.lower():
            return f"Encontrado: {producto['nombre']} - {producto['stock']} uds"
    return "Producto no encontrado"

def guardar_csv (productos) :
    with open("RUTA_CSV", "w", newline="", encoding="utf-8") as archivo :
        campos = ["nombre", "precio", "stock"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(productos)
    return "Datos guardados en inventario.csv"

opcion = ""
while opcion != "0":
    print("\n1.Listar productos")
    print("2.Añadir producto")
    print("3.Modificar stock")
    print("4.Buscra por nombre")
    print("5.Guardar en CSV")
    print("0.Salir")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        print(listar_productos(productos))
    elif opcion == "2":
        print(aniadir_producto(productos))
    elif opcion == "3":
        print(modificar_stock(productos))
    elif opcion == "4":
        print(buscar_producto(productos))
    elif opcion == "5":
        print(guardar_csv(productos))
    elif opcion == "0":
        print("Programa finalizado")
    else:
       print("Opcion no valida") 
    