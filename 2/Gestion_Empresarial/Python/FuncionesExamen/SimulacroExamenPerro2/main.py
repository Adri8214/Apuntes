"""UD1 · PT1 · PatitasAdopta. Menú y validaciones de entrada preparados."""
from pathlib import Path

from modelos import Perro, Protectora
from persistencia import cargar_perros, guardar_perros


def main():
    ruta = Path(__file__).with_name("perros.csv")
    protectora = Protectora()

    # Carga inicial de los perros desde el CSV.
    try:
        for perro in cargar_perros(ruta):
            protectora.registrar(perro)
    except (OSError, ValueError, KeyError) as error:
        print(f"No se ha podido cargar el CSV: {error}")

    opcion = ""
    while opcion != "0":
        print("\n========== PATITASADOPTA · PROTECTORA CANINA ==========")
        print("1. Listar perros")
        print("2. Registrar ingreso de un perro")
        print("3. Registrar adopción")
        print("4. Dar de baja un perro")
        print("5. Ver disponibles ordenados por edad")
        print("6. Mostrar estadísticas")
        print("7. Guardar en CSV")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            perros = protectora.listar()
            if not perros:
                print("No hay perros registrados.")
            else:
                for p in perros:
                    print(
                        f"{p.codigo} | {p.nombre} | {p.raza} | "
                        f"{p.edad} años | {p.peso:.1f} kg | {p.estado}"
                    )

        elif opcion == "2":
            codigo = input("Código: ").strip().upper()
            nombre = input("Nombre: ").strip()
            raza = input("Raza: ").strip()
            texto_edad = input("Edad (años): ").strip()
            texto_peso = input("Peso (kg): ").strip().replace(",", ".")

            if not codigo or not nombre or not raza:
                print("Error: código, nombre y raza no pueden estar vacíos.")
            else:
                try:
                    edad = int(texto_edad)
                    peso = float(texto_peso)
                except ValueError:
                    print("Error: la edad debe ser un entero y el peso un número.")
                else:
                    if not 0 <= edad <= 30:
                        print("Error: la edad debe estar entre 0 y 30 años.")
                    elif not 0 < peso < float("inf"):
                        print("Error: el peso debe ser positivo y finito.")
                    else:
                        perro = Perro(codigo, nombre, raza, edad, peso)
                        if protectora.registrar(perro):
                            print("Ingreso registrado correctamente.")
                        else:
                            print("Error: ya existe un perro con ese código.")

        elif opcion == "3":
            codigo = input("Código del perro adoptado: ").strip().upper()
            if not codigo:
                print("Error: el código no puede estar vacío.")
            elif protectora.adoptar(codigo):
                print("Perro marcado como ADOPTADO.")
            else:
                print("No se puede adoptar: código inexistente o ya adoptado.")

        elif opcion == "4":
            codigo = input("Código del perro a dar de baja: ").strip().upper()
            if not codigo:
                print("Error: el código no puede estar vacío.")
            elif protectora.dar_de_baja(codigo):
                print("Perro dado de baja correctamente.")
            else:
                print("No se puede dar de baja: código inexistente.")

        elif opcion == "5":
            disponibles = protectora.disponibles_por_edad()
            if not disponibles:
                print("No hay perros disponibles para adopción.")
            else:
                for p in disponibles:
                    print(f"{p.edad} años | {p.nombre} | {p.raza} | {p.codigo}")

        elif opcion == "6":
            datos = protectora.estadisticas()
            print(f"Total de perros: {datos['total']}")
            print(f"Disponibles: {datos['disponibles']}")
            print(f"Adoptados: {datos['adoptados']}")
            print(f"Peso medio de los disponibles: {datos['peso_medio_disponibles']:.2f} kg")
            pesado = datos["mas_pesado"]
            if pesado is None:
                print("Perro más pesado: no hay perros registrados.")
            else:
                print(f"Perro más pesado: {pesado.nombre} ({pesado.peso:.1f} kg)")

        elif opcion == "7":
            try:
                if guardar_perros(ruta, protectora.listar()):
                    print("Cambios guardados en perros.csv.")
                else:
                    print("No se han podido guardar los cambios.")
            except (OSError, ValueError) as error:
                print(f"Error al guardar el CSV: {error}")

        elif opcion == "0":
            print("Fin del programa.")
        else:
            print("Opción no válida. Elige un número entre 0 y 7.")


if __name__ == "__main__":
    main()