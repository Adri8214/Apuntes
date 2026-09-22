package RelacionEjercicios6;

import java.util.Scanner;

public class ejercicio1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int numeroAlumno = 1;
        int sumatorio = 0;
        int alumnosAprobados = 0;
        int alumnosSuspensos = 0;
        int nota;
        double media;

        System.out.println("Introduce la calificación del alumno " + numeroAlumno + " :");
        nota = scanner.nextInt();

        while (nota != -1) {
            sumatorio += nota;
            numeroAlumno++;

            if (nota < 5) {
                alumnosSuspensos++;
            }else{
                alumnosAprobados++;
            }

            System.out.println("Introduce la calificacion del alumno " + numeroAlumno + " :");
            nota = scanner.nextInt();
        }

        media = sumatorio / numeroAlumno;

        System.out.println("Hay " + alumnosAprobados + " alumnos aprobados y " + alumnosSuspensos + " alumnos suspensos");
        System.out.println("La calificacion media es de " + media);
        scanner.close();
    }
}
