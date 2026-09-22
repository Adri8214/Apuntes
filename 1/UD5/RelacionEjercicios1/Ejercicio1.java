package UD5.RelacionEjercicios1;

    public class Ejercicio1 {

        public static void main(String[] args) {

            Circulo c1 = new Circulo(5);
            Circulo c2 = new Circulo(1);

            System.out.println("Círculo 1");
            System.out.println("Radio: " + c1.radio);
            System.out.println("Área: " + c1.calcularArea());
            System.out.println("Perímetro: " + c1.calcularPerimetro());

            System.out.println();

            System.out.println("Círculo 2");
            System.out.println("Radio: " + c2.radio);
            System.out.println("Área: " + c2.calcularArea());
            System.out.println("Perímetro: " + c2.calcularPerimetro());
        }
    }

    class Circulo {

        double radio;
        final double PI = 3.1415;

        public Circulo(double radio) {
            this.radio = radio;
        }

        public double calcularArea() {
            return PI * radio * radio;
        }

        public double calcularPerimetro() {
            return 2 * PI * radio;
        }
    }



