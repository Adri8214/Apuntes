from pathlib import Path
import math

from modelos import Bicicleta, RegistroRobos
from persistencia import cargar_bicicletas, guardar_bicicletas


def main():
    ruta = Path(__file__).with_name("bicicletas.csv")
    registro = RegistroRobos()

    try:
        bicicletas = cargar_bicicletas(ruta)

        for bicicleta in bicicletas:
            if not registro.registrar(bicicleta):
                raise ValueError(
                    f"Código duplicado: {bicicleta.codigo}"
                )

    except (OSError, ValueError, KeyError) as error:
        print(f"No se ha podido cargar el CSV: {error}")

    opcion = ""

    while opcion != "0":
        print("\n========== BICIALERTA · REGISTRO DE ROBOS ==========")
        print("1. Listar bicicletas")
        print("2. Registrar un robo")
        print("3. Marcar bicicleta como recuperada")
        print("4. Buscar por propietario o modelo")
        print("5. Mostrar resumen")
        print("6. Guardar en CSV")
        print("0. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            bicicletas = registro.listar()

            if len(bicicletas) == 0:
                print("No hay bicicletas registradas.")
            else:
                for bicicleta in bicicletas:
                    print(bicicleta.ficha())

        elif opcion == "2":
            codigo = input("Código: ").strip().upper()
            propietario = input("Propietario: ").strip()
            modelo = input("Modelo: ").strip()
            importe = input("Valor (€): ").strip().replace(",", ".")

            if not codigo or not propietario or not modelo:
                print("Error: los campos no pueden estar vacíos.")
            else:
                try:
                    valor = float(importe)

                    if valor <= 0 or not math.isfinite(valor):
                        print("Error: el valor debe ser positivo y finito.")
                    else:
                        bicicleta = Bicicleta(
                            codigo, propietario, modelo, valor
                        )

                        if registro.registrar(bicicleta):
                            print("Robo registrado correctamente.")
                        else:
                            print("Error: ese código ya existe.")

                except ValueError:
                    print("Error: introduce un valor numérico válido.")

        elif opcion == "3":
            codigo = input("Código a recuperar: ").strip().upper()

            if registro.recuperar(codigo):
                print("Bicicleta marcada como RECUPERADA.")
            else:
                print("Código inexistente o bicicleta ya recuperada.")

        elif opcion == "4":
            texto = input("Texto a buscar: ").strip()

            if not texto:
                print("Error: el texto no puede estar vacío.")
            else:
                resultados = registro.buscar(texto)

                if len(resultados) == 0:
                    print("No se encontraron coincidencias.")
                else:
                    for bicicleta in resultados:
                        print(bicicleta.ficha())

        elif opcion == "5":
            datos = registro.resumen()

            print(f"Total de bicicletas: {datos['total']}")
            print(f"Robadas: {datos['robadas']}")
            print(f"Recuperadas: {datos['recuperadas']}")
            print(
                f"Valor pendiente: "
                f"{datos['valor_pendiente']:.2f} EUR"
            )

        elif opcion == "6":
            try:
                if guardar_bicicletas(ruta, registro.listar()):
                    print("Cambios guardados en bicicletas.csv.")
            except (OSError, ValueError) as error:
                print(f"Error al guardar el CSV: {error}")

        elif opcion == "0":
            print("Fin del programa.")

        else:
            print("Opción no válida. Elige un número entre 0 y 6.")


if __name__ == "__main__":
    main()