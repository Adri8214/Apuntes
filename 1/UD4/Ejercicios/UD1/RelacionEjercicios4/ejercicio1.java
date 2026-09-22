package RelacionEjercicios4;

import java.util.Scanner;

public class ejercicio1 {
    public static void main(String[] args) {
        final int TABLADEL10 = 10;
        Scanner scanner = new Scanner(System.in);

        int tabla;
        int multiplicacion = 0;

        System.out.println("Introduce el número: ");
        tabla = scanner.nextInt();
        scanner.close();

        for (int i = 1; i <= TABLADEL10; i++) {
            multiplicacion = tabla * i;
            System.out.println(tabla + " x " + i + " = " + multiplicacion);
        }
    }
}
