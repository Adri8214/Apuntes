package RelacionEjercicios2;
import java.util.Scanner;

public class ejercicio9 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numeroDeCaramelos = 0;
        int numeroDeNinios = 0;
        int caramelosPorNinio = 0;
        int restoDeCaramelos = 0;
        System.out.println("Introduce el numero de caramelos que tienes: ");
        numeroDeCaramelos = entrada.nextInt();

        System.out.println("Introduce el número de niños que hay: ");
        numeroDeNinios = entrada.nextInt();
        entrada.close();

        caramelosPorNinio = numeroDeCaramelos / numeroDeNinios;
        restoDeCaramelos = numeroDeCaramelos % numeroDeNinios;

        System.out.println(
                "A cada niño le tocan " + caramelosPorNinio + " y le han sobrado " + restoDeCaramelos + " caramelos");

    }
}
