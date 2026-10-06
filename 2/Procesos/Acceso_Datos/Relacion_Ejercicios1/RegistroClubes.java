import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.Scanner;

public class RegistroClubes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Path carpeta = Path.of("datos", "clubes.txt");

        int id = 0;

        while (id != -1) {
            String nombre;
            String ciudad;

            try {
                System.out.println("Introduce un id: ");
                id = sc.nextInt();
                sc.nextLine();

                if (id == -1) {
                    break;
                }

                System.out.println("Introduce el nombre: ");
                nombre = sc.nextLine();

                System.out.println("Introduce una ciudad: ");
                ciudad = sc.nextLine();

                Files.createDirectories(carpeta.getParent());
                try (BufferedWriter salida = Files.newBufferedWriter(carpeta, StandardCharsets.UTF_8,
                        StandardOpenOption.CREATE,
                        StandardOpenOption.APPEND)) {

                    salida.write("\n" + id + ";" + nombre + ";" + ciudad);
                }
            } catch (IOException e) {
                System.out.println("No se ha encontrado el archivo " + e.getMessage());
            }

            try (BufferedReader entrada = Files.newBufferedReader(carpeta, StandardCharsets.UTF_8)) {
                String linea;

                while ((linea = entrada.readLine()) != null) {
                    System.out.println(linea);
                }
            } catch (IOException e) {
                System.out.println("No se ha podido leer: " + e.getMessage());
            }
        }
        sc.close();
    }
}
