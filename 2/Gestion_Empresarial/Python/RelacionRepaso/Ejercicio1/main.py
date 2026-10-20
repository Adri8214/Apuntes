from modelos import FloristeriaGestor
from persistencia import guardar_productos, cargar_productos, guardar_ventas, cargar_ventas

def main():
    gestor = FloristeriaGestor()
    gestor.productos = cargar_productos()
    gestor.cargar_catalogo_inicial()
    gestor.ventas_cerradas = cargar_ventas()

    opcion = ""
    while opcion != "0":
        print("\n--- GESTIÓN FLORISTERÍA LILA ---")
        print("1) Ver productos")
        print("2) Alta producto")
        print("3) Reponer producto")
        print("4) Nueva venta / añadir líneas")
        print("5) Cerrar venta")
        print("6) Consultar ventas")
        print("7) Guardar")
        print("0) Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            if not gestor.productos:
                print("No hay productos disponibles.")
            else:
                for p in gestor.productos.values():
                    print(f"[{p.codigo}] {p.nombre} ({p.categoria}) - {p.precio:.2f}€ | Stock: {p.stock}")

        elif opcion == "2":
            codigo = input("Código del producto: ").strip()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            try:
                precio = float(input("Precio: "))
                stock = int(input("Stock inicial: "))
                exito, mensaje = gestor.alta_producto(codigo, nombre, categoria, precio, stock)
                print(mensaje)
            except ValueError:
                print("Error: El precio y el stock deben ser valores numéricos válidos.")

        elif opcion == "3":
            codigo = input("Código del producto a reponer: ").strip()
            try:
                cantidad = int(input("Cantidad a añadir: "))
                exito, mensaje = gestor.reponer_producto(codigo, cantidad)
                print(mensaje)
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")

        elif opcion == "4":
            if not gestor.venta_actual or gestor.venta_actual.cerrada:
                numero = input("Número de venta: ").strip()
                cliente = input("Cliente: ").strip()
                exito, mensaje = gestor.iniciar_venta(numero, cliente)
                print(mensaje)
                if not exito:
                    continue
            
            print(f"\nVenta actual - Cliente: {gestor.venta_actual.cliente} (Nº {gestor.venta_actual.numero})")
            print("Deje el código vacío si desea dejar/terminar la venta abierta por ahora.")
            codigo = input("Código de producto a añadir: ").strip()
            if codigo:
                try:
                    cantidad = int(input("Cantidad: "))
                    exito, mensaje = gestor.agregar_linea_venta(codigo, cantidad)
                    print(mensaje)
                except ValueError:
                    print("Error: La cantidad debe ser un número entero.")

        elif opcion == "5":
            if not gestor.venta_actual:
                print("No hay ninguna venta abierta actualmente.")
            else:
                v = gestor.venta_actual
                print(f"\n--- Detalle Venta Nº {v.numero} ({v.cliente}) ---")
                for l in v.lineas:
                    print(f"  * Producto: {l.producto} | Cantidad: {l.cantidad} | P.Unit: {l.precio_unitario:.2f}€")
                print(f"Subtotal: {v.subtotal:.2f}€")
                print(f"Total (con descuento si aplica): {v.total:.2f}€")
                
                confirmar = input("¿Desea cerrar esta venta? (s/n): ").strip().lower()
                if confirmar == 's':
                    exito, mensaje = gestor.cerrar_venta()
                    print(mensaje)
                else:
                    print("La venta permanece abierta.")

        elif opcion == "6":
            if not gestor.ventas_cerradas:
                print("No hay ventas cerradas registradas.")
            else:
                acumulado = 0.0
                for v in gestor.ventas_cerradas:
                    acumulado += v.total
                    print(f"Venta {v.numero} | Cliente: {v.cliente} | Subtotal: {v.subtotal:.2f}€ | Total: {v.total:.2f}€")
                    for l in v.lineas:
                        print(f"   -> {l.producto}: {l.cantidad} uds a {l.precio_unitario:.2f}€")
                print(f"\nImporte acumulado total de ventas cerradas: {acumulado:.2f}€")

        elif opcion == "7":
            guardar_productos(gestor.productos)
            guardar_ventas(gestor.ventas_cerradas)
            print("Datos guardados correctamente en los ficheros CSV.")

        elif opcion == "0":
            guardar_productos(gestor.productos)
            guardar_ventas(gestor.ventas_cerradas)
            print("Saliendo de la aplicación. ¡Hasta pronto!")

        else:
            print("Opción no válida. Introduzca un número del menú.")

if __name__ == "__main__":
    main()