package RelacionEjercicios3;

import java.util.Scanner;

public class ejercicio5 {
    public static void main(String[] args) {
        final int DIEZ = 10;
        final int VEINTE = 20;
         
        int numero = 0;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduzca el numero: ");
        numero = scanner.nextInt();
        scanner.close();

        if (numero >= DIEZ && numero <= VEINTE) {
            System.out.println("El número está entre 10 y 20");
        } else{
            System.out.println("El número no está entre 10 y 20");
        }
    }
}
