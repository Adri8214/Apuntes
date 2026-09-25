import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class InspectorFichero {
    public static void main(String[] args) {
        Path datos = Path.of("datos");
        Path archivo = datos.resolve("clubes.txt");

        
        System.out.println("Ruta absoluta: " + archivo.toAbsolutePath());

        try {

            if (Files.exists(archivo)) {
                System.out.println("El archivo existe");
                System.out.println("Tamaño del archivo: " + Files.size(archivo));
            }else {
                System.out.println("El archivo no existe");
            }

            
            
        } catch (IOException e) {
            System.out.println("No se puede acceder al archivo " + e.getMessage());
        }
    }
}
