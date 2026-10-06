import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Path carpeta = Path.of("datos", "alumnos.csv");

        int id;
        int idUsuario;
        String nombre;
        String curso;
        boolean encontrado = false;
        
        // Introducir en un try catch id, nombre y curso (Lineas 32-34) y convertirlo en un Integer
        try {
            List<String> Listaalumnos = Files.readAllLines(carpeta, StandardCharsets.UTF_8);
            
            System.out.println("Introduce un id: ");
            idUsuario = entrada.nextInt();
            entrada.nextLine();

            for (int i = 1; i < Listaalumnos.size(); i++) {
                String[] campos = Listaalumnos.get(i).split(";", -1);

                if (campos.length == 3) {
                    id = Integer.parseInt(campos[0]);
                    nombre = campos[1];
                    curso = campos[2];

                    if (id == idUsuario) {
                        encontrado = true;
                        System.out.println("Nombre: " + nombre + "\nCurso: " + curso);
                        break;
                    }
                
                } else {
                    System.out.println("Debe de contener 3 campos");
                }
            }

        } catch (IOException e) {

        }
        entrada.close();
    }
}
