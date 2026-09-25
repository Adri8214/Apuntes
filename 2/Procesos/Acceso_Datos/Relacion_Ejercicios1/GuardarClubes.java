import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

public class GuardarClubes {
    public static void main(String[] args) {
        Path carpeta = Path.of("datos", "clubes.txt");


        try {
            Files.createDirectories(carpeta.getParent());  
            
            try(BufferedWriter salida = Files.newBufferedWriter(carpeta, StandardCharsets.UTF_8)) {
                salida.write("1;Granada CF;Granada");
                salida.newLine();
                salida.write("2;Málaga CF;Málaga");
                salida.newLine();
                salida.write("3;Cádiz CF;Cádiz");
                salida.close();
            }
        } catch (IOException e) {
            System.err.println("No se ha encontrado el archivo " + e.getMessage());
        }
    }
}
