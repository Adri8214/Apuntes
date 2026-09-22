package RelacionEjercicios6;

import java.util.Scanner;

public class ejercicio6 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        String numero1 = "";
        String numero2 = "";
        String operacionUsuario = "";
        int resultadoOperacion = 0;

        int n1 = 0;
        int n2 = 0;

        while (!numero1.equalsIgnoreCase("SALIR")
                && !numero2.equalsIgnoreCase("SALIR")
                && !operacionUsuario.equalsIgnoreCase("SALIR")) {

            System.out.print("Introduce el primer número: ");
            numero1 = scanner.nextLine();

            if (!numero1.equalsIgnoreCase("SALIR")) {

                n1 = Integer.parseInt(numero1);

                System.out.print("Introduce el segundo número: ");
                numero2 = scanner.nextLine();

                if (!numero2.equalsIgnoreCase("SALIR")) {

                    n2 = Integer.parseInt(numero2);

                    System.out.print("Introduce la operación: ");
                    operacionUsuario = scanner.nextLine();

                    if (!operacionUsuario.equalsIgnoreCase("SALIR")) {

                        if (operacionUsuario.equals("+")) {
                            resultadoOperacion = n1 + n2;
                        } else if (operacionUsuario.equals("-")) {
                            resultadoOperacion = n1 - n2;
                        } else if (operacionUsuario.equals("*")) {
                            resultadoOperacion = n1 * n2;
                        } else if (operacionUsuario.equals("/")) {
                            resultadoOperacion = n1 / n2;
                        } else {
                            System.out.println("Operación no válida");
                        }

                        System.out.println(
                                "El resultado de " + n1 + operacionUsuario + n2 + " es " + resultadoOperacion);
                    }
                }
            }
        }

        System.out.println("Programa finalizado.");
        scanner.close();
    }
}
