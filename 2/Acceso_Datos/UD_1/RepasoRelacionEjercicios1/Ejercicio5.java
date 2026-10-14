import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

public class Ejercicio5 {
    public static void main(String[] args) {
        Path archivo = Path.of("datos", "clubes.txt");

        try {
            Files.createDirectories(archivo.getParent());

            try (BufferedWriter salida = Files.newBufferedWriter(archivo, StandardCharsets.UTF_8)) {
                salida.write("1;Granada CF;Granada");
                salida.newLine();
                salida.write("2;Málaga CF;Málaga");
                salida.newLine();
                salida.write("3;Cádiz CF;Cádiz");
                salida.newLine();
                
            } catch (IOException e) {
                System.out.println("No se ha podido guardar el archivo " + e.getMessage());
            }
        } catch (IOException e) {
            System.err.println("No se ha podido encontrar el archivo " + e.getMessage());
        }
    }
}
