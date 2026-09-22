package UD5.RelacionEjercicios1;

    public class Ejercicio3 {
        public static void main(String[] args) {
            Alumno a1 = new Alumno("Manueh", "Programación", 8);

            System.out.println("Alumno: " + a1.nombre);
            System.out.println("Materia: " + a1.materia);
            System.out.println("Calificación " + a1.calificacion);
            System.out.println("Aprobado / Suspenso: " + a1.aprobo());
        }
    }

    class Alumno {
        String nombre;
        String materia;
        double calificacion;

        public Alumno(String nombre, String materia, double calificacion) {
            this.nombre = nombre;
            this.materia = materia;
            this.calificacion = calificacion;
        }

        public boolean aprobo() {
            if (calificacion >= 6) {
                return true;
            } else {
                return false;
            }
        }
    }
