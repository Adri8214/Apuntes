package UD4.Ejercicios.UD2.RelacionEjercicios2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        ArrayList<String> tareas = new ArrayList<>(Arrays.asList("tarea1", "tarea2", "tarea3"));
        ArrayList<Boolean> completadas = new ArrayList<>(Arrays.asList(false, true, false));
        ArrayList<String> pendientes = new ArrayList<>();
        ArrayList<String> hechas = new ArrayList<>();

        String opcion = "";
        String nuevaTarea;
        String buscarTarea;
        boolean encontrado;

        while (!opcion.equals("5")) {
            System.out.println("1. Añadir tarea\n" +
                               "2. Marcar completada\n" +
                               "3. Ver pendientes\n" +
                               "4. Ver completadas\n" +
                               "5. Salir"
            );

            opcion = scanner.nextLine();

            if (opcion.equals("1")) {

                System.out.println("Nueva tarea: ");
                nuevaTarea = scanner.nextLine();
                tareas.add(nuevaTarea);
                completadas.add(false);

            } else if (opcion.equals("2")) {
                
                System.out.println("Nombre de la tarea: ");
                buscarTarea = scanner.nextLine();
                encontrado = false;

                for (int i = 0; i < tareas.size(); i++) {
                    if (tareas.get(i).equals(buscarTarea)) {
                        encontrado = true;
                        completadas.set(i, true);
                    }
                }

                if (!encontrado) {
                    System.out.println("No encotrada");
                }

            } else if (opcion.equals("3")) {
                pendientes.clear();
                for (int i = 0; i < completadas.size(); i++) {
                    if (!completadas.get(i)) {
                        pendientes.add(tareas.get(i));
                    }
                }

                System.out.println("Pendientes: " + pendientes);

            } else if (opcion.equals("4")) {
                hechas.clear();
                for (int i = 0; i < completadas.size(); i++) {
                    if (completadas.get(i)) {
                        hechas.add(tareas.get(i));
                    }
                }

                System.out.println("Completadas: " + hechas);

            } else if (opcion.equals("5")) {
                System.out.println("Programa finalizado");
                
            } else {
                System.out.println("Introduce una opción válida");
            }             
        }

        scanner.close();
    }
}
