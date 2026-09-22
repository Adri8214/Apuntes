package UD4.Ejercicios.UD2.RelacionEjercicios2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> jugadores = new ArrayList<>(Arrays.asList("Jugador1", "Jugador2", "Jugador3", "Jugador4", "Jugador5"));
        ArrayList<Integer> puntuaciones = new ArrayList<>(Arrays.asList(120, 200, 150, 180, 220));
        String opcion = "";
        String nombreJugadorNuevo;
        int puntuacionJugadorNuevo;

        while (!opcion.equals("3")) {
            System.out.println("1. Añadir jugador\n" + 
                               "2. Ver jugadores\n" +
                               "3. Salir");

            opcion = scanner.nextLine();

            if (opcion.equals("1")) {
                System.out.println("Introduce el nombre del jugador nuevo: ");
                nombreJugadorNuevo = scanner.nextLine();
                jugadores.add(nombreJugadorNuevo);

                System.out.println("Introduce la puntuación del nuevo jugador: ");
                puntuacionJugadorNuevo = scanner.nextInt();
                scanner.nextLine();
                puntuaciones.add(puntuacionJugadorNuevo);

            } else if (opcion.equals("2")) {
                for (int i = 0; i < puntuaciones.size(); i++) {
                    System.out.println(jugadores.get(i) + " - " + puntuaciones.get(i));
                }
            } else if (opcion.equals("3")) {
                System.out.println("Programa finalizado");
            } else {
                System.out.println("Introduce una opción válida");
            }
        }

        scanner.close();

    }
}
