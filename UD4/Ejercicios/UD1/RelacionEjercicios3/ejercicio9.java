package RelacionEjercicios3;

import java.util.Scanner;

public class ejercicio9 {
public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);
    
    int numero;
    int digitoDecenas;
    int digitoUnidades;
    int suma = 0;

    System.out.println("Introduzca un número de dos dígitos: ");
    numero = scanner.nextInt();
    scanner.close();

    if (numero >= 10 && numero <= 99) {
        digitoDecenas = numero / 10;
        digitoUnidades = numero % 10;
        suma = digitoDecenas + digitoUnidades;
        System.out.println("El número tiene dos cifras, la suma de cifras es: " + suma);    
    } else{
        System.out.println("El número no tiene dos cifras");
    }
  }
}
