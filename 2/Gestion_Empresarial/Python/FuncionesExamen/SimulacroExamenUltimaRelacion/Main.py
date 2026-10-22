"""Punto de entrada: Tienda Canina Huellas. Toda la interacción por consola está aquí."""
from pathlib import Path

from Modelo import Producto, Tienda, productos_iniciales
from Persistencia import cargar_productos, cargar_ventas, guardar_productos, guardar_ventas


def texto_producto(p):
    """Devuelve (no imprime) la línea de texto de un producto."""
    return f"{p.codigo} | {p.nombre} | {p.categoria} | {p.precio:.2f} € | stock: {p.stock}"


def texto_venta(venta):
    """Devuelve (no imprime) el detalle completo de una venta."""
    filas = [f"Venta nº {venta.numero} · Cliente: {venta.cliente}"]
    for linea in venta.lineas:
        filas.append(
            f"  {linea.producto.codigo} | {linea.producto.nombre} | "
            f"{linea.cantidad} x {linea.precio_unitario:.2f} € = {linea.importe():.2f} €"
        )
    filas.append(f"Subtotal: {venta.subtotal():.2f} €")
    if venta.descuento() > 0:
        filas.append(f"Descuento (10 %): -{venta.descuento():.2f} €")
    filas.append(f"TOTAL: {venta.total():.2f} €")
    return "\n".join(filas)


def main():
    carpeta = Path(__file__).parent
    ruta_productos = carpeta / "productos.csv"
    ruta_ventas = carpeta / "ventas.csv"
    tienda = Tienda()

    # ---- Carga inicial del catálogo ----
    try:
        productos = cargar_productos(ruta_productos)
    except FileNotFoundError:
        print("No existe productos.csv: se usan los productos iniciales.")
        productos = productos_iniciales()
    except (OSError, ValueError, KeyError) as error:
        print(f"No se ha podido cargar productos.csv ({error}): se usan los productos iniciales.")
        productos = productos_iniciales()
    for producto in productos:
        tienda.alta_producto(producto)

    # ---- Carga inicial del historial de ventas ----
    try:
        for venta in cargar_ventas(ruta_ventas, tienda.productos):
            tienda.incorporar_venta(venta)
    except FileNotFoundError:
        pass  # primera ejecución: todavía no hay ventas guardadas
    except (OSError, ValueError, KeyError) as error:
        print(f"No se ha podido cargar ventas.csv: {error}")

    opcion = ""
    while opcion != "0":
        print("\n========== TIENDA CANINA HUELLAS ==========")
        print("1. Ver productos")
        print("2. Alta de producto")
        print("3. Reponer stock")
        print("4. Nueva venta / añadir líneas")
        print("5. Cerrar venta")
        print("6. Consultar ventas")
        print("7. Guardar en CSV")
        print("8. Cancelar venta actual")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            productos = tienda.listar_productos()
            if not productos:
                print("No hay productos en el catálogo.")
            else:
                for p in productos:
                    print(texto_producto(p))

        elif opcion == "2":
            codigo = input("Código: ").strip().upper()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            precio = input("Precio (€): ").strip().replace(",", ".")
            stock = input("Stock inicial: ").strip()
            try:
                producto = Producto(codigo, nombre, categoria, precio, stock)
            except ValueError as error:
                print(f"Error: {error}.")
            else:
                if tienda.alta_producto(producto):
                    print("Producto dado de alta correctamente.")
                else:
                    print("Error: ya existe un producto con ese código.")

        elif opcion == "3":
            codigo = input("Código del producto: ").strip().upper()
            texto = input("Unidades a reponer: ").strip()
            try:
                cantidad = int(texto)
            except ValueError:
                print("Error: la cantidad debe ser un número entero.")
            else:
                resultado = tienda.reponer(codigo, cantidad)
                if resultado == "OK":
                    print(f"Reposición realizada. Nuevo stock: {tienda.buscar_producto(codigo).stock}")
                elif resultado == "NO_EXISTE":
                    print("Error: el producto no existe.")
                else:
                    print("Error: la cantidad debe ser mayor que cero.")

        elif opcion == "4":
            if tienda.venta_actual is None:
                cliente = input("Nombre del cliente: ").strip()
                if tienda.abrir_venta(cliente) == "OK":
                    print(f"Venta nº {tienda.venta_actual.numero} abierta.")
                else:
                    print("Error: el nombre del cliente no puede estar vacío.")
            else:
                print(f"Continúas la venta nº {tienda.venta_actual.numero}.")

            if tienda.venta_actual is not None:
                anadiendo = True
                while anadiendo:
                    codigo = input("Código del producto (vacío para terminar): ").strip().upper()
                    if not codigo:
                        anadiendo = False
                    else:
                        texto = input("Cantidad: ").strip()
                        try:
                            cantidad = int(texto)
                        except ValueError:
                            print("Error: la cantidad debe ser un número entero.")
                        else:
                            resultado = tienda.anadir_linea(codigo, cantidad)
                            if resultado == "OK":
                                print("Línea añadida. Stock restante: "
                                      f"{tienda.buscar_producto(codigo).stock}")
                            elif resultado == "NO_EXISTE":
                                print("Error: el producto no existe.")
                            elif resultado == "CANTIDAD_INVALIDA":
                                print("Error: la cantidad debe ser mayor que cero.")
                            elif resultado == "STOCK_INSUFICIENTE":
                                print("Error: no hay stock suficiente. No se ha modificado nada.")
                            else:
                                print("Error: no hay ninguna venta abierta.")
                print(texto_venta(tienda.venta_actual))

        elif opcion == "5":
            venta = tienda.venta_actual
            resultado = tienda.cerrar_venta()
            if resultado == "OK":
                print("Venta cerrada y añadida al historial.")
                print(texto_venta(venta))
            elif resultado == "VENTA_VACIA":
                print("No se puede cerrar una venta sin líneas (añade productos o cancélala).")
            else:
                print("No hay ninguna venta abierta.")

        elif opcion == "6":
            if tienda.venta_actual is not None:
                print("--- VENTA EN CURSO (sin cerrar) ---")
                print(texto_venta(tienda.venta_actual))
            if not tienda.ventas_cerradas:
                print("No hay ventas cerradas.")
            else:
                print("--- VENTAS CERRADAS ---")
                for venta in tienda.ventas_cerradas:
                    print(texto_venta(venta))
                    print("-" * 40)
                print(f"Importe acumulado de las ventas cerradas: {tienda.importe_acumulado():.2f} €")

        elif opcion == "7":
            if tienda.venta_actual is not None:
                print("Cierra o cancela la venta en curso antes de guardar.")
            else:
                try:
                    guardar_productos(ruta_productos, tienda.listar_productos())
                    guardar_ventas(ruta_ventas, tienda.ventas_cerradas)
                    print("Catálogo y ventas guardados en productos.csv y ventas.csv.")
                except OSError as error:
                    print(f"Error al guardar los CSV: {error}")

        elif opcion == "8":
            if tienda.cancelar_venta():
                print("Venta cancelada: las unidades reservadas han vuelto al stock.")
            else:
                print("No hay ninguna venta abierta que cancelar.")

        elif opcion == "0":
            if tienda.cancelar_venta():
                print("La venta en curso se ha cancelado y el stock se ha devuelto.")
            print("Fin del programa.")
        else:
            print("Opción no válida. Elige un número entre 0 y 8.")


if __name__ == "__main__":
    main()