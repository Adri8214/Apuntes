// Crea las carpetas datos y datos/copias mediante Files.createDirectories(...)
// Crea los archivos vacíos datos/clubles.txt y datos/copias/respaldo.txt únicamente cuando aún no existan
// Muestra para cada archivo si existe y cuál es su tamaño en bytes.
// Ejecuta el programa dos veces.Después escribe manualmente una frase en respaldo.txt y ejecutalo otra vez: esa frase debe conservarse

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class PrepararCarpetas {

    public static void main(String[] args) {
        
        Path carpeta1 = Path.of("datos");
        Path carpeta2 = carpeta1.resolve("copias");

        Path archivo1 = carpeta1.resolve("clubes.txt");
        Path archivo2 = carpeta2.resolve("respaldo.txt");

        try {
            Files.createDirectories(carpeta1);
            Files.createDirectories(carpeta2);

            if (Files.notExists(archivo1)) {
                Files.createFile(archivo1);
            }
            
            if (Files.notExists(archivo2)) {
                Files.createFile(archivo2);
            }

            System.out.println("--- ARCHIVO 1 ---");
            System.out.println("¿Existe?: " + Files.exists(archivo1));
            System.out.println("Tamaño: " + Files.size(archivo1));

            System.out.println();

            System.out.println("--- ARCHIVO 2 ---");
            System.out.println("¿Existe?: " + Files.exists(archivo2));
            System.out.println("Tamaño: " + Files.size(archivo2));

        } catch (IOException e) {
            
            System.err.println("No se pudo acceder al archivo " + e.getMessage());
        }
    }
}
