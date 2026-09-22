import java.util.Scanner;

public class ejercicio6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Introduzca su edad: ");
        int edad = entrada.nextInt();

        int edadSegundos = edad * (365 * 24 * 60 * 60);

        System.out.println("Has vivido al menos " + edadSegundos + " segundos");
        entrada.close();
    }
}
