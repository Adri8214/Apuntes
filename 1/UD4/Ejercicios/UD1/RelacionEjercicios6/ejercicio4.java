package RelacionEjercicios6;

import java.util.Scanner;

public class ejercicio4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double consumo100km, combustibleDisponible,combustibleConsumido;
        double precioLitro, precioViaje;
        int numeroViaje = 1;
        double kilometrosViaje;

        System.out.println("Introduce el combustible inicial: ");
        combustibleDisponible = scanner.nextDouble();

        System.out.println("Precio del litro de combustible: ");
        precioLitro = scanner.nextDouble();

        System.out.println("Consumo cada 100km:");
        consumo100km = scanner.nextDouble();

        while (combustibleDisponible > 0) {
            System.out.println("\nIntroduce los kilómetros del viaje " + numeroViaje + ": ");
            kilometrosViaje = scanner.nextDouble();

            combustibleConsumido = kilometrosViaje * consumo100km / 100;

            if (combustibleConsumido <= combustibleDisponible) {
                precioViaje = combustibleConsumido * precioLitro;
                combustibleDisponible -= combustibleConsumido;

                System.out.println("Precio del viaje: " + precioViaje);
                System.out.println("Combustible restante: " + combustibleDisponible);

                numeroViaje++;
            } else {
                System.out.println("Combustible insuficiente");
                combustibleDisponible = 0;
            }
        }
        scanner.close();
    }
}
