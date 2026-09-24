// Crea una clase RutasProyecto que represente las rutas de la carpeta datos , el fichero clubes.txt y una subcarpeta llamada copias . No debes crear todavía ningún archivo ni carpeta.
// Construye la ruta de datos con Path.of(...) .
// Obtén las otras dos rutas utilizando resolve(...) .
// Muestra en consola las tres rutas relativas y sus correspondientes rutas absolutas con toAbsolutePath() .
// Comprueba: observa que construir o mostrar una ruta no crea por sí mismo un archivo. 
// Ejecuta la clase desde el directorio de trabajo de tu proyecto.

import java.nio.file.Path;

public class RutasProyecto {
    public static void main(String[] args) {

        Path Datos = Path.of("datos");
        Path fichero = Datos.resolve("clubes.txt");
        Path copias = Datos.resolve("copias");

        System.out.println("--- RUTAS ABSOLUTAS --- ");
        System.out.println("Ruta1: " + Datos.toAbsolutePath());
        System.out.println("Ruta2: " + fichero.toAbsolutePath());
        System.out.println("Ruta3: " + copias.toAbsolutePath());

        System.out.println();

        System.out.println("--- RUTAS RELATIVAS --- ");
        System.out.println("Ruta1: " + Datos);
        System.out.println("Ruta2: " + fichero);
        System.out.println("Ruta3: " + copias);
    }
}
