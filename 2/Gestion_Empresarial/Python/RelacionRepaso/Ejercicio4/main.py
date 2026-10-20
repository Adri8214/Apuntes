from modelos import ServicioTecnicoGestor, Reparacion
from persistencia import guardar_trabajos, cargar_trabajos

def main():
    gestor = ServicioTecnicoGestor()
    gestor.trabajos = cargar_trabajos()

    opcion = ""
    while opcion != "0":
        print("\n--- SERVICIO TÉCNICO ---")
        print("1) Listar trabajos")
        print("2) Alta reparación")
        print("3) Alta asistencia remota")
        print("4) Cambiar estado")
        print("5) Buscar / filtrar trabajos")
        print("6) Resumen")
        print("7) Guardar")
        print("0) Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            if not gestor.trabajos:
                print("No hay trabajos registrados.")
            else:
                for t in gestor.trabajos.values():
                    tipo_str = "Reparación" if isinstance(t, Reparacion) else "Asistencia Remota"
                    print(f"[{t.codigo}] {tipo_str} | Cliente: {t.cliente} | Horas: {t.horas} | Estado: {t.estado} | Importe: {t.calcular_importe():.2f}€")

        elif opcion == "2":
            codigo = input("Código del trabajo: ").strip()
            cliente = input("Nombre del cliente: ").strip()
            try:
                horas = float(input("Número de horas: "))
                precio_pieza = float(input("Precio de la pieza (€): "))
                exito, mensaje = gestor.alta_trabajo("reparacion", codigo, cliente, horas, precio_pieza)
                print(mensaje)
            except ValueError:
                print("Error: Las horas y el precio de la pieza deben ser numéricos[cite: 2].")

        elif opcion == "3":
            codigo = input("Código del trabajo: ").strip()
            cliente = input("Nombre del cliente: ").strip()
            try:
                horas = float(input("Número de horas: "))
                exito, mensaje = gestor.alta_trabajo("remota", codigo, cliente, horas)
                print(mensaje)
            except ValueError:
                print("Error: Las horas deben ser un número válido[cite: 2].")

        elif opcion == "4":
            codigo = input("Código del trabajo a actualizar: ").strip()
            print("Estados disponibles: pendiente, en curso, finalizado")
            nuevo_estado = input("Nuevo estado: ").strip()
            exito, mensaje = gestor.cambiar_estado_trabajo(codigo, nuevo_estado)
            print(mensaje)

        elif opcion == "5":
            cliente_f = input("Filtrar por cliente (dejar vacío para omitir): ").strip()
            tipo_f = input("Filtrar por tipo ('reparacion' o 'remota', dejar vacío para omitir): ").strip()
            estado_f = input("Filtrar por estado ('pendiente', 'en curso', 'finalizado', dejar vacío para omitir): ").strip()
            
            resultados = gestor.buscar_filtrar(cliente_f, tipo_f, estado_f)
            if not resultados:
                print("No se encontraron trabajos con los criterios especificados.")
            else:
                print(f"\nResultados encontrados ({len(resultados)}):")
                for tipo_str, t in resultados:
                    print(f"[{t.codigo}] Tipo: {tipo_str.upper()} | Cliente: {t.cliente} | Horas: {t.horas} | Estado: {t.estado} | Importe: {t.calcular_importe():.2f}€")

        elif opcion == "6":
            conteo, importe_finalizados = gestor.obtener_resumen()
            print("\n--- RESUMEN DEL SERVICIO TÉCNICO ---")
            print("Número de trabajos por estado:")
            for estado, cantidad in conteo.items():
                print(f"  - {estado.capitalize()}: {cantidad}")
            print(f"Importe total acumulado de trabajos finalizados: {importe_finalizados:.2f}€")

        elif opcion == "7":
            guardar_trabajos(gestor.trabajos)
            print("Trabajos guardados correctamente en 'trabajos.csv'.")

        elif opcion == "0":
            guardar_trabajos(gestor.trabajos)
            print("Saliendo de la aplicación. ¡Hasta pronto!")

        else:
            print("Opción no válida. Introduzca un número del menú.")

if __name__ == "__main__":
    main()