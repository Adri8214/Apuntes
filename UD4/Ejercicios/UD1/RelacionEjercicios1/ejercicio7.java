package RelacionEjercicios1;
import java.util.Scanner;

public class ejercicio7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Introdzuca su peso en Kg: ");
        double pesoKg = entrada.nextDouble();
        
        System.out.println("Introduzca su altura en metros: ");
        double altura = entrada.nextDouble();

        double IMC = pesoKg / (altura * altura);

        System.out.println("Tu IMC es: " + IMC);
        entrada.close();
    }
}
