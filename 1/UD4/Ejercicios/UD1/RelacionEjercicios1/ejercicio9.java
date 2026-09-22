package RelacionEjercicios1;
import java.util.Scanner;

public class ejercicio9 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Introduce el numero de caramelos que tienes: ");
        int numeroCramelos = entrada.nextInt();

        System.out.println("Introduce el número de niños que hay: ");
        int numeroNinios = entrada.nextInt();

        int caramelosPorNinio = numeroCramelos / numeroNinios;
        int restoDeCaramelos = numeroCramelos % numeroNinios;

        System.out.println("A cada niño le tocan " + caramelosPorNinio + " y le han sobrado " + restoDeCaramelos + " caramelos");
        
        entrada.close();
    }
}
