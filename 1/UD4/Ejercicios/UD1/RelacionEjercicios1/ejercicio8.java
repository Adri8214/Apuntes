package RelacionEjercicios1;
import java.util.Scanner;

public class ejercicio8 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Introduzca la distancia recorrida en km: ");
        int km = entrada.nextInt();

        System.out.println("Introduzca el tiempo que ha tardado en minutos: ");
        int tiempoMinutos = entrada.nextInt();

        double tiempoHoras = tiempoMinutos / 60;
        double velocidad = km / tiempoHoras;

        System.out.println("Su velocidad media ha sido: " + velocidad + "km/h");

        entrada.close();
    }
}
