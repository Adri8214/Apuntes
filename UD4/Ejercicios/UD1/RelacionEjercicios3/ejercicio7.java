package RelacionEjercicios3;

import java.util.Scanner;

public class ejercicio7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double numero1;
        double numero2;
        String operador;
        boolean division0 = false;
        double resultado = 0;

        System.out.println("Introduzca un número: ");
        numero1 = scanner.nextInt();

        System.out.println("Introduzca otro número: ");
        numero2 = scanner.nextInt();

        System.out.println("Introduzca el operador: ");
        operador = scanner.next();
        scanner.close();

        if (operador.equals("+")) {
            resultado = numero1 + numero2;
        } else if (operador.equals("-")) {
            resultado = numero1 - numero2;
        } else if (operador.equals("*")) {
            resultado = numero1 * numero2;
        } else if (operador.equals("/")) {
            if (numero2 != 0) {
                resultado = numero1 / numero2;
            } else{
                System.out.println("No es posible dividir entre 0");
                division0 = true;
            }
        } else{
            System.out.println("Operador incorrecto");
        }

        if (!division0) {
            System.out.println("El resultado de " + numero1 + " " + operador + " " +numero2 + " es " + resultado);
        } else{
            System.out.println("Vuelva a probar con valores correctos");
        }
    }
}
