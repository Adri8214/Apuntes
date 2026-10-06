import java.io.IOException;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;

public class ListarDatos {
    public static void main(String[] args) {
        
        Path carpeta = Path.of("datos");
        

        try (DirectoryStream<Path> elementos = Files.newDirectoryStream(carpeta)) {
            
            for (Path elemento : elementos) {
                if (Files.isRegularFile(elemento)) {
                    System.out.println(elemento.getFileName());
                }
            }

        } catch (IOException e) {
            System.err.println("No se ha podido acceder al archivo " + e.getMessage());
        }
    }
}
