package RelacionEjercicios2;
import java.util.Scanner;

public class ejercicio5 {
    public static void main(String[] args) {

        final double GRAVEDADLUNA = 0.165;
        Scanner entrada = new Scanner(System.in);

        double pesoUsuario = 0;
        double pesoLuna = 0;

        System.out.println("Introduzca su peso: ");
        pesoUsuario = entrada.nextDouble();
        
        pesoLuna = pesoUsuario * GRAVEDADLUNA;
        System.out.printf("En la luna pesarías %.2f Kg", pesoLuna);
        entrada.close();
    }
}