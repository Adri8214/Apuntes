package UD5.RelacionEjercicios1;

    public class Ejercicio5 {
        public static void main(String[] args) {
            Termometro t1 = new Termometro(50);
            System.out.println("La temperatura actual es de: " + t1.temperatura);
            System.out.println("La temperatura pasada a grados farenheit es de: " + t1.convertirAFarenheit());
        }
    }

    class Termometro {
        double temperatura;

        public Termometro(double temperatura) {
            this.temperatura = temperatura;
        }

        public double convertirAFarenheit() {
            return (temperatura * 9 / 5) + 32;
        }
    }