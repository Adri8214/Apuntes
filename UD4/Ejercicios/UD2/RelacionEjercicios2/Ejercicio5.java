package UD4.Ejercicios.UD2.RelacionEjercicios2;

import java.util.ArrayList;
import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> nombres = new ArrayList<>();
        ArrayList<Double> calificaciones = new ArrayList<>();

        String opcion = "";
        String nombreNuevo;
        double notaNueva;
        double suma;
        double max;
        String nombreMax;
        double min;
        String nombreMin;

        while (!opcion.equals("5")) {
            System.out.println("1. Añadir estudiante\n" +
                               "2. Ver media\n" + 
                               "3. Nota más alta\n" + 
                               "4. Nota más baja\n" + 
                               "5. Salir"  

            );

            opcion = scanner.nextLine();

            if (opcion.equals("1")) {
                System.out.println("Nombre del alumno: ");
                nombreNuevo = scanner.nextLine();
                nombres.add(nombreNuevo);

                System.out.println("Calificacion del alumno: ");
                notaNueva = scanner.nextDouble();
                scanner.nextLine();
                calificaciones.add(notaNueva);

            } else if (opcion.equals("2")) {
                suma = 0;
                for (int i = 0; i < calificaciones.size(); i++) {
                    suma += calificaciones.get(i);
                }

                System.out.println("La media es " + (suma / calificaciones.size()));
            
            } else if (opcion.equals("3")) {
                max = calificaciones.get(0);
                nombreMax = nombres.get(0);
                
                for (int i = 0; i < calificaciones.size(); i++) {
                    if (calificaciones.get(i) > max) {
                        max = calificaciones.get(i);
                        nombreMax = nombres.get(i);
                    }
                }

                System.out.println("Máxima calificación: " + nombreMax + "(" + max + ")");

            } else if(opcion.equals("4")){
                min = calificaciones.get(0);
                nombreMin = nombres.get(0);

                for (int i = 0; i < calificaciones.size(); i++) {
                    if (calificaciones.get(i) < min) {
                        min = calificaciones.get(i);
                        nombreMin = nombres.get(i);
                    }
                }

                System.out.println("Mínima calificación: " + nombreMin + "(" + min + ")");

            } else if (opcion.equals("5")) {
                System.out.println("Programa finalizado");
            } else {
                System.out.println("Introduce una opción válida");
            }
        }
        scanner.close();
    }
}
