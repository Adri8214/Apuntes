from modelos import CentroTalleres
from persistencia import guardar_datos, cargar_datos

def main():
    centro = CentroTalleres()
    cargar_datos(centro)
    centro.cargar_datos_iniciales()

    opcion = ""
    while opcion != "0":
        print("\n--- CENTRO DE TALLERES ---")
        print("1) Ver participantes")
        print("2) Alta participante")
        print("3) Inscribir en taller")
        print("4) Cancelar inscripción")
        print("5) Ver taller (plazas y ocupación)")
        print("6) Buscar participante")
        print("7) Guardar")
        print("0) Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            if not centro.participantes:
                print("No hay participantes registrados.")
            else:
                print("\n--- LISTA DE PARTICIPANTES ---")
                for p in centro.participantes.values():
                    print(f"Email: {p.email} | Nombre: {p.nombre}")

        elif opcion == "2":
            email = input("Correo electrónico del participante: ").strip()
            nombre = input("Nombre completo: ").strip()
            exito, mensaje = centro.alta_participante(email, nombre)
            print(mensaje)

        elif opcion == "3":
            print("\nTalleres disponibles:")
            for t in centro.talleres.values():
                print(f"  [{t.codigo}] {t.titulo} (Plazas totales: {t.plazas})")
            
            email = input("Email del participante: ").strip()
            codigo_taller = input("Código del taller: ").strip()
            exito, mensaje = centro.inscribir_participante(email, codigo_taller)
            print(mensaje)

        elif opcion == "4":
            email = input("Email del participante: ").strip()
            codigo_taller = input("Código del taller: ").strip()
            exito, mensaje = centro.cancelar_inscripcion(email, codigo_taller)
            print(mensaje)

        elif opcion == "5":
            print("\nTalleres existentes:")
            for t in centro.talleres.values():
                print(f"  [{t.codigo}] {t.titulo}")
            
            codigo_taller = input("Introduzca el código del taller a consultar: ").strip()
            resultado, mensaje = centro.consultar_taller(codigo_taller)
            if not resultado:
                print(mensaje)
            else:
                t = resultado["taller"]
                print(f"\n--- Taller: {t.titulo} [{t.codigo}] ---")
                print(f"Plazas totales: {t.plazas}")
                print(f"Plazas libres: {resultado['plazas_libres']}")
                print(f"Porcentaje de ocupación: {resultado['porcentaje_ocupacion']:.1f}%")
                print("Participantes inscritos:")
                if not resultado["inscritos"]:
                    print("  Ninguno.")
                else:
                    for p in resultado["inscritos"]:
                        print(f"  - {p.nombre} ({p.email})")

        elif opcion == "6":
            fragmento = input("Introduce parte del nombre o email a buscar: ").strip()
            resultados = centro.buscar_participante(fragmento)
            if not resultados:
                print("No se encontró ningún participante con ese criterio.")
            else:
                print(f"\nResultados encontrados ({len(resultados)}):")
                for res in resultados:
                    p = res["participante"]
                    print(f"\nParticipante: {p.nombre} ({p.email})")
                    if not res["talleres"]:
                        print("  Talleres inscritos: Ninguno.")
                    else:
                        print("  Talleres inscritos:")
                        for tal in res["talleres"]:
                            print(f"    - {tal.titulo} [{tal.codigo}]")

        elif opcion == "7":
            guardar_datos(centro)
            print("Datos guardados correctamente en los ficheros CSV.")

        elif opcion == "0":
            guardar_datos(centro)
            print("Saliendo de la aplicación. ¡Hasta pronto!")

        else:
            print("Opción no válida. Introduzca un número del menú.")

if __name__ == "__main__":
    main()