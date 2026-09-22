package UD5.RelacionEjercicios1;

    public class Ejercicio4 {
        public static void main(String[] args) {
            Auto a1 = new Auto("Mercedes", "amg", 50);
            
            System.out.println("Marca: " + a1.marca);
            System.out.println("Modelo: " + a1.modelo);
            System.out.println("Velocidad Actual " + a1.velocidadActual);
            a1.acelerar(50);
            a1.frenar(20);
            System.out.println("Velocidad actual: " + a1.velocidadActual);
        }
    }

    class Auto {
        String marca;
        String modelo;
        double velocidadActual;

        public Auto(String marca, String modelo, double velocidadActual){
            this.marca = marca;
            this.modelo = modelo;
            this.velocidadActual = velocidadActual;
        }

        public void acelerar(double cantidad){
            if (cantidad < 0) {
                System.out.println("Debes ingresar una velocidad positiva");
            } else {
                velocidadActual += cantidad;
            }
        }

        public void frenar(double cantidad) {
            if (cantidad < 0) {
                System.out.println("Debes ingresar una cantidad positiva");
            } else if (cantidad > velocidadActual) {
                System.out.println("La velocidad de frenado debe de ser mayor que la velocidad actual");
            } else {
                velocidadActual -= cantidad;
            }
        }
    }
