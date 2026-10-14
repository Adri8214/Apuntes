import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Ejercicio2 {
    public static void main(String[] args) {
        Path ruta = Path.of("datos");    
        Path ruta2 = Path.of("datos/copias"); 
        
        Path archivo1 = Path.of("datos/clubes.txt");
        Path archivo2 = Path.of("datos/copias/respaldo.txt");

        try {
            Files.createDirectories(ruta);
            Files.createDirectories(ruta2);

            if (!Files.exists(archivo1)) {
                Files.createFile(archivo1);
            }

            if (!Files.exists(archivo2)) {
                Files.createFile(archivo2);
            }

            System.out.println("=== Archivo 1 ===");
            
            System.out.println("¿Existe?: " + Files.exists(archivo1));
            System.out.println("Tamaño en bytes: " + Files.size(archivo1) );
            
            
            System.out.println("=== Archivo 2 ===");
            
            System.out.println("¿Existe?: " + Files.exists(archivo2));
            System.out.println("Tamaño en bytes: " + Files.size(archivo2));


        } catch (IOException e) {
            System.err.println("No se ha podido acceder al archivo");
        }
    }
}

