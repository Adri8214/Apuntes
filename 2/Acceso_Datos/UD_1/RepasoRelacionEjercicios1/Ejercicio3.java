import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Ejercicio3 {
    public static void main(String[] args) {
        Path archivo = Path.of("datos", "clubes.txt");

        System.out.println("Ruta Absoluta: ");
        System.out.println(archivo.toAbsolutePath());

        if (Files.exists(archivo)) {
            System.out.println("El archivo existe");

            try {
            long tamanio = Files.size(archivo);
            System.out.println("El archivo tiene un tamaño de " + tamanio + "Bytes");

            } catch (IOException e) {
                System.err.println("No se ha podido encontrar el archivo " + e.getMessage());
            }
        } else if (Files.notExists(archivo)) {
            System.out.println("El archivo no existe");
        } else {
            System.out.println("No se puede determinar si el archivo existe");
        }
    }
}
