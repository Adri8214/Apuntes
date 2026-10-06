import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int id;
        boolean encontrado = false;

        Path archivo = Path.of("datos", "reservas.csv");

        
        try {
            List<String> listaReservas = Files.readAllLines(archivo, StandardCharsets.UTF_8);
            List<String> nuevaListaReservas = new ArrayList<>();
            
            System.out.println("Introduce el id de la reserva que desea cancelar: ");
            id = entrada.nextInt();
            entrada.nextLine();

            for (String lista1 : listaReservas) {
                String[] campos = lista1.split(";", -1);
                
                if (campos.length == 3) {
                    
                    try {
                         
                        if (id == Integer.parseInt(campos[0])) {
                            String lineaNueva = campos[0] + ";" + campos[1] + ";" + campos[2];
                            nuevaListaReservas.add(lineaNueva);
                            encontrado = true;
                        }
                        
                    } catch (NumberFormatException e) {
                        System.out.println("Debe de haber como mínimo 3 campos");
                    }
                }
            }

        } catch (IOException e) {
            System.out.println("No se ha podido encontrar el archivo " + e.getMessage());
        }
    }
}
