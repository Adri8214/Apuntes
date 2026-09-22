import java.util.Scanner;

public class ejercicio5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Introduzca su peso: ");
        double pesoEnLaTierra = entrada.nextDouble();
        
        double pesoEnLaLuna = pesoEnLaTierra * 0.165;
        System.out.println("En la luna pesarías " + pesoEnLaLuna + "Kg");
        entrada.close();
    }
}