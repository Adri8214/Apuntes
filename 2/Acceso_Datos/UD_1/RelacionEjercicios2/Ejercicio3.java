import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Path archivo = Path.of("datos", "inventario.csv");

        int id = 0;
        int idUsuario;
        int stockNuevo;
        int stock;
        boolean encontrado = false;

        try {

            List<String> listaInventario = Files.readAllLines(archivo, StandardCharsets.UTF_8);
            List<String> nuevalista = new ArrayList<>();

            nuevalista.add(listaInventario.get(0));

            System.out.println("Introduce un id: ");
            idUsuario = entrada.nextInt();
            entrada.nextLine();

            System.out.println("Introduce un número de stock: ");
            stockNuevo = entrada.nextInt();
            entrada.nextLine();


            for (int i = 1; i < listaInventario.size(); i++) {

                String linea = listaInventario.get(i);
                String[] campos = linea.split(";", -1);

                if (campos.length == 3) {

                    try {
                        id = Integer.parseInt(campos[0]);
                        stock = Integer.parseInt(campos[2]);
                        
                        if (id == idUsuario) {
                         String lineaNueva = campos[0] + ";" + campos [1] + ";" + stockNuevo;
                         nuevalista.add(lineaNueva);
                         encontrado = true;   
                        } else {
                            nuevalista.add(linea);
                        }
                    } catch (NumberFormatException e) {
                        nuevalista.add(linea);
                    }

                } else {
                    nuevalista.add(linea);
                }
            }

            System.out.println("Lista original: " );
            for (String linea : listaInventario) {
                System.out.println(linea);
            }

            System.out.println("\nLista actualizada: ");
            for (String linea : nuevalista) {
                System.out.println(linea);
            }

            
            if (encontrado) {
                Files.write(archivo, nuevalista, StandardCharsets.UTF_8);
            } else {
                System.out.println("El id no existe. No se puede modificar el archivo");
            }

        } catch (IOException e) {
            System.out.println("No se ha podido encontar el archivo " + e.getMessage());
        }
        entrada.close();
    }
}