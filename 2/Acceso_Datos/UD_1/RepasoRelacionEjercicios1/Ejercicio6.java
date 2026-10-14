import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

public class Ejercicio6 {
    public static void main(String[] args) {
        Path archivo = Path.of("datos", "clubes.txt");

        if (!Files.notExists(archivo)) {
            System.out.println("El archivo existe");
        }else {
            System.out.println("El archivo no existe");
        }

        try (BufferedReader entrada = Files.newBufferedReader(archivo, StandardCharsets.UTF_8)) {
            String linea;
            while ((linea = entrada.readLine()) != null) {
                System.out.println(linea);
            }

        } catch (IOException e) {
            System.out.println("No se pudo leer: " + e.getMessage());
        }
    }
}
