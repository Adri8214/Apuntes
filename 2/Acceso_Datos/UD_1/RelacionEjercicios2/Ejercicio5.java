import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.List;
import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Path archivo = Path.of("datos", "biblioteca.csv");

        String id, titulo, autor;
        int idNumerico;
        boolean esValido = true;

        try (Scanner entrada = new Scanner(System.in)) {

            if (!Files.exists(archivo)) {
                System.out.println("No existe el archivo " + archivo);
                return;
            }

            List<String> lineas = Files.readAllLines(archivo, StandardCharsets.UTF_8);

            System.out.println("Introduce el id del nuevo libro: ");
            id = entrada.nextLine();

            System.out.println("Introduce el titulo del libro");
            titulo = entrada.nextLine();

            System.out.println("Introduce el autor del libro");
            autor = entrada.nextLine();

            try {
                idNumerico = Integer.parseInt(id);

                if (idNumerico <= 0) {
                    System.err.println("El id debería de ser mayor que 0");
                    esValido = false;   
                }
                
                if (titulo.isBlank()) {
                    System.err.println("El titulo no puede estar vacío");
                    esValido = false;
                }

                if (autor.isBlank()) {
                    System.err.println("El autor no puede estar vacío");
                    esValido = false;
                }

                if (esValido) {
                    
                    for (String linea : lineas) {
                        
                        String[] datosLibro = linea.split(";", -1);

                        if (datosLibro.length >= 3) {
                            
                            String idExistente = datosLibro[0].trim();
                            String tituloExistente = datosLibro[1].trim();

                            if (idExistente.equals(id.trim())) {
                                System.err.println("Ya existe un libro con ese id");
                                esValido = false;
                                break;
                            }

                            if (tituloExistente.equalsIgnoreCase(titulo.trim())) {
                                System.err.println("Ya existe un libro con ese titulo");
                                esValido = false;
                                break;
                            }

                        }
                    }
                }

                if (esValido) {
                    
                    String nuevaLinea = idNumerico + "," + titulo.trim() + "," + autor.trim();
                    Files.writeString(archivo, nuevaLinea, StandardCharsets.UTF_8);
                }

                System.out.println("Libro añadido correctamente");

            } catch (NumberFormatException e) {
                System.err.println("El id debería de ser un número");
            }

        } catch (IOException e) {
            System.out.println("No se ha podido encontrar el archivo");
        }
    }
}
