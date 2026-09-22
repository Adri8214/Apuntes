package UD4.Ejercicios.UD2.RelacionEjercicios2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> productos = new ArrayList<>(Arrays.asList("Manzanas", "Plátanos", "Leche", "Pan", "Huevos", "Azúcar", "Harina", "Arroz", "Pasta", "Café"));
        ArrayList<Double> precios = new ArrayList<>(Arrays.asList(1.20, 0.80, 1.50, 1.00, 2.00, 1.10, 0.90, 0.70, 1.30, 3.00));

        String productoUsuario = "";
        int cantidadProducto = 0;
        double subtotal;
        double total = 0;
        boolean encontrado;
        while (!productoUsuario.equalsIgnoreCase("FIN")) {
            System.out.println("Introduzca el nombre del producto: ");
            productoUsuario = scanner.next();

            if (!productoUsuario.equalsIgnoreCase("FIN")) {
                System.out.println("Introduzca la cantidad comprada: ");
                cantidadProducto = scanner.nextInt();
                scanner.nextLine();
            }

            encontrado = false;
            for (int i = 0; i < productos.size() && !encontrado; i++) {
                if (productos.get(i).equals(productoUsuario)) {
                    encontrado = true;
                    subtotal = precios.get(i) * cantidadProducto;
                    total += subtotal;

                    System.out.println(productoUsuario + " - " + cantidadProducto + ": " + subtotal + "€");
                }
            }
        }

        scanner.close();

        System.out.println("TOTAL: " + total + "€");
    }
}
