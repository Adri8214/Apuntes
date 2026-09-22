package UD4.Ejercicios.UD2.RelacionEjercicios2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Ejercicio8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> nombreReservas = new ArrayList<>(Arrays.asList("Laura", "Victoria", "Pedro", "Alejandro"));
        ArrayList<Integer> cantidadPersonas = new ArrayList<>(Arrays.asList(2, 5, 3, 7));

        String opcion = "";
        String nombre;
        int personas;
        int total;
        boolean encontrado = false;
        String mensaje;

        while (!opcion.equals("5")) {
            System.out.println("1. Añadir reserva\n" +
                               "2. Ver reservas\n" +
                               "3. Total personas\n" +
                               "4. Cancelar\n" +
                               "5. Salir" 
            );

            opcion = scanner.nextLine();

            if (opcion.equals("1")) {
                
                System.out.println("Nombre: ");
                nombre = scanner.nextLine();
                nombreReservas.add(nombre);

                System.out.println("Número de personas");
                personas = scanner.nextInt();
                scanner.nextLine();
                cantidadPersonas.add(personas);

            } else if (opcion.equals("2")) {
                mensaje = "";
                System.out.println("Reservas: ");
                for (int i = 0; i < nombreReservas.size(); i++) {
                    mensaje += nombreReservas.get(i) + " - " + cantidadPersonas.get(i) + "\n";
                }
                System.out.println(mensaje);

            } else if (opcion.equals("3")) {
                total = 0;
                for (int i = 0; i < cantidadPersonas.size(); i++) {
                    total += cantidadPersonas.get(i);
                }
                System.out.println(total);

            } else if (opcion.equals("4")) {
                System.out.println("Nombre a cancelar: ");
                nombre = scanner.nextLine();

                encontrado = false;
                for (int i = 0; i < nombreReservas.size() && ! encontrado; i++) {
                    if (nombreReservas.get(i).equalsIgnoreCase(nombre)) {
                        encontrado = true;
                        nombreReservas.remove(i);
                        cantidadPersonas.remove(i);
                    }
                }
            } else if (opcion.equals("5")) {
                System.out.println("Programa finalizado");
            } else {
                System.out.println("Introduce una opción válida");
            }
        }
        scanner.close();
    }
}
