import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Ejercicio1 {
    public static void main(String[] args) {
        Path carpeta = Path.of("datos", "videojuegos.csv");
        int id;

        try {
            
            List<String> videojuegos = Files.readAllLines(carpeta, StandardCharsets.UTF_8);

            for (int i = 1; i < videojuegos.size(); i++) {
                String linea = videojuegos.get(i);

                String[] campos = linea.split(";", -1);

                
                if (campos.length == 3) {
                    try {
                        id = Integer.parseInt(campos[0]);
                        String titulo = campos[1];
                        String plataforma = campos[2];

                        System.out.println("[" + id + "] " + titulo  + " - " + plataforma);
                    } catch (NumberFormatException e) {
                        System.out.println("El id no es válido " + e.getMessage());
                    }
                } else {
                    System.out.println("No tiene exactamente tres campos");
                }
            }

        } catch (IOException e) {
            System.out.println("No se ha encontrado el archivo " + e.getMessage());
        }
    }    
}
