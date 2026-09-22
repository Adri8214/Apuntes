package UD4.Ejercicios.UD2.RelacionEjercicios2;

import java.util.ArrayList;
import java.util.Scanner;

public class Ejercicio7 {
    public static void main(String[] args) {
        final int DIAS_MES = 30;
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> nombreGastos = new ArrayList<>();
        ArrayList<Integer> cantidadGastos = new ArrayList<>();

        String opcion = "";
        String nombre;
        int cantidad;
        int total;
        int posMax;
        int posMin;
        double promedioDiario = 0;
        while (!opcion.equals("5")) {
            System.out.println("1. Añadir gasto\n" +
                               "2. Ver total\n" +
                               "3. Ver máximo y minimo\n" +
                               "4. Promedio diario\n" +
                               "5. Salir" 
            );            

            opcion = scanner.nextLine();

            if (opcion.equals("1")) {
                System.out.println("Nombre del gasto: ");
                nombre = scanner.nextLine();
                nombreGastos.add(nombre);

                System.out.println("Cantidad: ");
                cantidad = scanner.nextInt();
                scanner.nextLine();
                cantidadGastos.add(cantidad);

            } else if (opcion.equals("2")) {
                total = 0;
                for (int i = 0; i < cantidadGastos.size(); i++) {
                    total += cantidadGastos.get(i);
                }
                System.out.println("Total: " + total + "€");
            } else if (opcion.equals("3")) {
                posMax = 0;
                posMin = 0;

                for (int i = 0; i < cantidadGastos.size(); i++) {
                    if (cantidadGastos.get(i) > cantidadGastos.get(posMax)) {
                        posMax = i;
                    }

                    if (cantidadGastos.get(i) < cantidadGastos.get(posMin)) {
                        posMin = i;
                    }
                }

                System.out.println("Mayor " + nombreGastos.get(posMax) + " - " + cantidadGastos.get(posMax) + "€");
                System.out.println("Menor " + nombreGastos.get(posMin) + " - " + cantidadGastos.get(posMin) + "€");

            } else if (opcion.equals("4")) {
                total = 0;
                for (int i = 0; i < cantidadGastos.size(); i++) {
                    total += cantidadGastos.get(i);
                }
                promedioDiario = total / DIAS_MES;
                System.out.println("Promedio diario: " + promedioDiario);

            } else if (opcion.equals("5")) {
                System.out.println("Programa finalizado");
            } else {
                System.out.println("Introduce una opción válida");
            }
        }
        scanner.close();
    }
}
