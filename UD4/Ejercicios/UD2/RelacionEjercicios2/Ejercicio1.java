package UD4.Ejercicios.UD2.RelacionEjercicios2;

import java.util.ArrayList;
import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        final int DIAS_SEMANA = 7;
        double temperaturaSolicitada;
        String opcion = "";
        double sumatorioTemperaturas = 0;
        double temperaturaMedia;

        ArrayList<Double> temperaturas = new ArrayList<>();

        for (int i = 1; i <= DIAS_SEMANA; i++) {
            System.out.println("Inserte la temperatura del día " + i + ":");
            temperaturaSolicitada = scanner.nextDouble();
            temperaturas.add(temperaturaSolicitada);
        }

        double temperaturaMaxima;
        double temperaturaMinima;

        while (!opcion.equals("4")) {

            System.out.println("1. Mostrar la temperatura más alta registrada\n" +
                    "2. Mostrar la temperatura más baja registrada\n" +
                    "3. Calcular la temperatura promedio de la semana\n" +
                    "4. Salir del programa");

            opcion = scanner.next();

            if (opcion.equals("1")) {

                temperaturaMaxima = temperaturas.get(0);

                for (int i = 0; i < temperaturas.size(); i++) {
                    if (temperaturas.get(i) > temperaturaMaxima) {
                        temperaturaMaxima = temperaturas.get(i);
                    }
                }
                System.out.println("La temperatura más alta es de " + temperaturaMaxima + " grados\n");

            } else if (opcion.equals("2")) {

                temperaturaMinima = temperaturas.get(0);

                for (int i = 0; i < temperaturas.size(); i++) {
                    if (temperaturas.get(i) < temperaturaMinima) {
                        temperaturaMinima = temperaturas.get(i);
                    }
                }

                System.out.println("La temperatura mínima es de " + temperaturaMinima + " grados\n");

            } else if (opcion.equals("3")) {
                sumatorioTemperaturas = 0;
                for (int i = 0; i < temperaturas.size(); i++) {
                    sumatorioTemperaturas += temperaturas.get(i);
                }

                temperaturaMedia = sumatorioTemperaturas / temperaturas.size();

                System.out.println("La temperatura media es de " + temperaturaMedia + " grados\n");

            } else if (opcion.equals("4")) {
                System.out.println("Programa finalizado");
            } else {
                System.out.println("Debes introducir una opción válida");
            }
        }

        scanner.close();
    }
}
