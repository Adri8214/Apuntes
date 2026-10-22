"""Lectura/escritura de CSV. Sin print() ni input()."""
import csv

from Modelo import Producto, Venta

CAMPOS_PRODUCTOS = ["codigo", "nombre", "categoria", "precio", "stock"]
# Una fila por línea de venta; las ventas se reconstruyen agrupando por "numero".
CAMPOS_VENTAS = ["numero", "cliente", "codigo_producto", "cantidad", "precio_unitario"]


def cargar_productos(ruta):
    """Devuelve la lista de Producto del CSV. Lanza ValueError si hay datos inválidos o códigos repetidos."""
    productos = []
    codigos = set()
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != CAMPOS_PRODUCTOS:
            raise ValueError("Las columnas de productos.csv no tienen el formato esperado")
        for fila in lector:
            producto = Producto(
                fila["codigo"], fila["nombre"], fila["categoria"],
                fila["precio"], fila["stock"],
            )
            if producto.codigo in codigos:
                raise ValueError(f"Código repetido en productos.csv: {producto.codigo}")
            codigos.add(producto.codigo)
            productos.append(producto)
    return productos


def guardar_productos(ruta, productos):
    """Escribe el catálogo completo; devuelve True al terminar."""
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_PRODUCTOS)
        escritor.writeheader()
        for p in productos:
            escritor.writerow({
                "codigo": p.codigo, "nombre": p.nombre, "categoria": p.categoria,
                "precio": p.precio, "stock": p.stock,
            })
    return True


def cargar_ventas(ruta, productos):
    """Reconstruye las ventas cerradas. `productos` es un dict codigo -> Producto.

    Si alguna fila es inválida o referencia un producto inexistente se lanza
    ValueError y no se devuelve ninguna venta (carga todo o nada).
    """
    ventas = {}
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != CAMPOS_VENTAS:
            raise ValueError("Las columnas de ventas.csv no tienen el formato esperado")
        for fila in lector:
            try:
                numero = int(fila["numero"])
            except (TypeError, ValueError):
                raise ValueError("Número de venta no válido en ventas.csv") from None

            codigo = (fila["codigo_producto"] or "").strip().upper()
            producto = productos.get(codigo)
            if producto is None:
                raise ValueError(f"La venta {numero} usa un producto inexistente: {codigo}")

            cliente = (fila["cliente"] or "").strip()
            venta = ventas.get(numero)
            if venta is None:
                venta = Venta(numero, cliente)
                ventas[numero] = venta
            elif venta.cliente != cliente:
                raise ValueError(f"La venta {numero} tiene clientes distintos")

            venta.agregar_linea(producto, fila["cantidad"], fila["precio_unitario"])

    return sorted(ventas.values(), key=lambda v: v.numero)


def guardar_ventas(ruta, ventas):
    """Escribe las ventas cerradas (una fila por línea); devuelve True al terminar."""
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_VENTAS)
        escritor.writeheader()
        for venta in ventas:
            for linea in venta.lineas:
                escritor.writerow({
                    "numero": venta.numero,
                    "cliente": venta.cliente,
                    "codigo_producto": linea.producto.codigo,
                    "cantidad": linea.cantidad,
                    "precio_unitario": linea.precio_unitario,
                })
    return True