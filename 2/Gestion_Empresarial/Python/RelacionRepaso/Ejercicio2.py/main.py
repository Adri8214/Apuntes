from modelos import Coleccion
from persistencia import guardar_coleccion, cargar_coleccion

def main():
    coleccion = Coleccion()
    coleccion.cartas = cargar_coleccion()
    coleccion.cargar_inicial()

    opcion = ""
    while opcion != "0":
        print("\n--- COLECCIÓN DE CARTAS POKÉMON ---")
        print("1) Listar cartas")
        print("2) Añadir carta")
        print("3) Eliminar carta")
        print("4) Buscar / filtrar cartas")
        print("5) Intercambiar carta")
        print("6) Estadísticas")
        print("7) Guardar")
        print("0) Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            if not coleccion.cartas:
                print("La colección está vacía.")
            else:
                for c in coleccion.cartas.values():
                    print(f"[{c.codigo}] {c.nombre} | Tipo: {c.tipo} | Rareza: {c.rareza} | Valor: {c.valor:.2f}€")

        elif opcion == "2":
            codigo = input("Código de la carta: ").strip()
            nombre = input("Nombre: ").strip()
            tipo = input("Tipo: ").strip()
            rareza = input("Rareza: ").strip()
            try:
                valor = float(input("Valor (€): "))
                exito, mensaje = coleccion.alta_carta(codigo, nombre, tipo, rareza, valor)
                print(mensaje)
            except ValueError:
                print("Error: El valor debe ser numérico[cite: 2].")

        elif opcion == "3":
            codigo = input("Código de la carta a eliminar: ").strip()
            exito, mensaje = coleccion.eliminar_carta(codigo)
            print(mensaje)

        elif opcion == "4":
            termino = input("Buscar por nombre o tipo (dejar en blanco para omitir): ").strip()
            rareza = input("Filtrar por rareza (dejar en blanco para omitir): ").strip()
            resultados = coleccion.buscar_filtrar(termino, rareza)
            if not resultados:
                print("No se encontraron cartas con esos criterios.")
            else:
                print(f"\nSe encontraron {len(resultados)} carta(s):")
                for c in resultados:
                    print(f"[{c.codigo}] {c.nombre} | Tipo: {c.tipo} | Rareza: {c.rareza} | Valor: {c.valor:.2f}€")

        elif opcion == "5":
            codigo_antiguo = input("Código de la carta que entregas (antigua): ").strip()
            print("Introduce los datos de la nueva carta a recibir:")
            nuevo_codigo = input("Nuevo código: ").strip()
            nuevo_nombre = input("Nuevo nombre: ").strip()
            nuevo_tipo = input("Nuevo tipo: ").strip()
            nueva_rareza = input("Nueva rareza: ").strip()
            try:
                nuevo_valor = float(input("Nuevo valor (€): "))
                exito, mensaje = coleccion.intercambiar_carta(
                    codigo_antiguo, nuevo_codigo, nuevo_nombre, nuevo_tipo, nueva_rareza, nuevo_valor
                )
                print(mensaje)
            except ValueError:
                print("Error: El valor debe ser numérico[cite: 2].")

        elif opcion == "6":
            total_cartas, valor_total, conteo_rareza = coleccion.obtener_estadisticas()
            print(f"\n--- ESTADÍSTICAS DE LA COLECCIÓN ---")
            print(f"Número total de cartas: {total_cartas}")
            print(f"Valor total de la colección: {valor_total:.2f}€")
            print("Cartas por rareza:")
            for rareza, cantidad in conteo_rareza.items():
                print(f"  - {rareza}: {cantidad}")

        elif opcion == "7":
            guardar_coleccion(coleccion.cartas)
            print("Colección guardada correctamente en 'cartas.csv'[cite: 4].")

        elif opcion == "0":
            guardar_coleccion(coleccion.cartas)
            print("Saliendo de la aplicación. ¡Hasta pronto!")

        else:
            print("Opción no válida. Introduzca un número del menú.")

if __name__ == "__main__":
    main()