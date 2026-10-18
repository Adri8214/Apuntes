import csv
from pathlib import Path

RUTA_CSV = Path(__file__).with_name("inventario.csv")

def convertir_entero(texto, minimo=0):
    try:
        numero = int(texto)
    except ValueError:
        return None
    if numero >= minimo:
        return numero
    else:
        return None

def convertir_precio(texto):
    try:
        precio = float(texto)
    except ValueError:
        return None
    if precio >= 0:
        return precio
    else:
        return None

def encontrar_producto(productos, nombre):
    for producto in productos:
        if producto["nombre"].casefold() == nombre.casefold():
            return producto
    return None

def aniadir_producto(productos ,nombre, precio, stock):
    if not nombre:
        return "nombre vacío"
    if encontrar_producto(productos, nombre) is not None:
        return "duplicado"
    productos.append({"nombre": nombre, "precio": precio, "stock": stock})
    return "añadido"

def modificar_stock(productos, nombre, nuevo_stock):
    producto = encontrar_producto(productos, nombre)

    if producto is None:
        return False
    producto["stock"] = nuevo_stock
    return True

def buscar_productos(productos, texto):
    busqueda = texto.casefold()
    resultados = []
    for producto in productos:
        if busqueda in producto["nombre"].casefold():
            resultados.append(producto)
    return resultados

def formatear_producto(numero, producto):
    return (
        f"{numero}. {producto['nombre']} | " 
        f"{producto['precio']:.2f} EUR | Stock: {producto['stock']}"
    )

def guardar_csv(productos):
    with open(RUTA_CSV, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio", "stock"])
        escritor.writeheader()
        escritor.writerows(productos)
    return len(productos)


def main():

    productos =[
        {"nombre": "Boligrafo", "precio": 2.5, "stock": 300},
        {"nombre": "Lapiz", "precio": 1.3, "stock": 120},
        {"nombre": "Folio", "precio": 0.50, "stock": 500}
    ]

    opcion = ""

    while opcion != "0":
        print("\n1.Listar productos")
        print("\n2.Añadir producto")
        print("\n3.Modificar stock")
        print("\n4.Buscar por nombre")
        print("\n5.Guardar en CSV")
        print("\n0.Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            if not productos:
                print("No hay productos")
            for numero, producto in enumerate(productos, start=1):
                print(formatear_producto(numero, producto))

        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion != "0":
            print("Opción no válida")

if __name__ == "__main__":
    main()