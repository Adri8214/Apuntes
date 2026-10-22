"""UD1 · PT1 · CanAlerta. Menú y validaciones de entrada preparados."""
from pathlib import Path
 
from modelo import Perro, RegistroPerdidos
from persistencia import cargar_perros, guardar_perros
 
 
def main():
    ruta = Path(__file__).with_name("perros.csv")
    registro = RegistroPerdidos()
 
    # Carga inicial de los perros desde el CSV.
    try:
        for perro in cargar_perros(ruta):
            registro.registrar(perro)
    except (OSError, ValueError, KeyError) as error:
        print(f"No se ha podido cargar el CSV: {error}")
 
    opcion = ""
    while opcion != "0":
        print("\n========== CANALERTA · REGISTRO DE PERROS PERDIDOS ==========")
        print("1. Listar perros")
        print("2. Registrar una pérdida")
        print("3. Marcar perro como encontrado")
        print("4. Buscar por propietario o raza")
        print("5. Mostrar resumen")
        print("6. Guardar en CSV")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()
 
        if opcion == "1":
            perros = registro.listar()
            if not perros:
                print("No hay perros registrados.")
            else:
                for perro in perros:
                    print(
                        f"{perro.codigo} | {perro.propietario} | {perro.raza} | "
                        f"{perro.recompensa:.2f} € | {perro.estado}"
                    )
 
        elif opcion == "2":
            codigo = input("Código: ").strip().upper()
            propietario = input("Propietario: ").strip()
            raza = input("Raza: ").strip()
            importe = input("Recompensa (€): ").strip().replace(",", ".")
 
            if not codigo or not propietario or not raza:
                print("Error: código, propietario y raza no pueden estar vacíos.")
            else:
                try:
                    recompensa = float(importe)
                except ValueError:
                    print("Error: introduce un valor numérico.")
                else:
                    if not 0 < recompensa < float("inf"):
                        print("Error: la recompensa debe ser positiva y finita.")
                    else:
                        perro = Perro(codigo, propietario, raza, recompensa)
                        if registro.registrar(perro):
                            print("Pérdida registrada correctamente.")
                        else:
                            print("Error: ya existe un perro con ese código.")
 
        elif opcion == "3":
            codigo = input("Código del perro encontrado: ").strip().upper()
            if not codigo:
                print("Error: el código no puede estar vacío.")
            elif registro.encontrar(codigo):
                print("Perro marcado como ENCONTRADO.")
            else:
                print("No se puede marcar: código inexistente o ya encontrado.")
 
        elif opcion == "4":
            texto = input("Texto a buscar: ").strip()
            if not texto:
                print("Error: el texto de búsqueda no puede estar vacío.")
            else:
                resultados = registro.buscar(texto)
                if not resultados:
                    print("No se encontraron coincidencias.")
                else:
                    for perro in resultados:
                        print(f"{perro.codigo} | {perro.propietario} | {perro.raza} | {perro.estado}")
 
        elif opcion == "5":
            datos = registro.resumen()
            print(f"Total de perros: {datos['total']}")
            print(f"Perdidos: {datos['perdidos']}")
            print(f"Encontrados: {datos['encontrados']}")
            print(f"Recompensa pendiente: {datos['recompensa_pendiente']:.2f} €")
 
        elif opcion == "6":
            try:
                guardado = guardar_perros(ruta, registro.listar())
                if guardado:
                    print("Cambios guardados en perros.csv.")
                else:
                    print("No se han podido guardar los cambios.")
            except (OSError, ValueError) as error:
                print(f"Error al guardar el CSV: {error}")
 
        elif opcion == "0":
            print("Fin del programa.")
        else:
            print("Opción no válida. Elige un número entre 0 y 6.")
 
 
if __name__ == "__main__":
    main()
 

