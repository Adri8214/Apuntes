import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Path archivo = Path.of("datos", "biblioteca.csv");

        String id;

        if (!Files.exists(archivo)) {
            System.out.println("No existe el archivo " + archivo);
            entrada.close();
            return;
        }

        System.out.println("Introduce el id del nuevo libro: ");
        id = entrada.nextLine();

        try {
            List<String> lineas = Files.readAllLines(archivo, StandardCharsets.UTF_8)
        

        } catch (IOException e) {
            System.out.println("No se ha podido encontrar el archivo");
        }
    }
}
