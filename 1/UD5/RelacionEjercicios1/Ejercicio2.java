package UD5.RelacionEjercicios1;

    public class Ejercicio2 {
        public static void main(String[] args) {
            cuentaBancaria cuentaBancaria1 = new cuentaBancaria("Mariano", 500);
            System.out.println("Titular de la cuenta: " + cuentaBancaria1.titular);
            System.out.println("Saldo de la cuenta: " + cuentaBancaria1.saldo);
        }
    }

    class cuentaBancaria {
        String titular;
        double saldo;

        public cuentaBancaria(String titular, double saldo) {
            this.titular = titular;
            this.saldo = saldo;
        }

        public void depositar(double cantidad) {
            if (cantidad > 0) {
                saldo += cantidad;
            } else {
                System.out.println("La cantidad a depositar debe de ser positiva");
            }
        }

        public void retirar(double cantidad) {
            if (cantidad <= 0) {
                System.out.println("La cantidad ingresada no puede ser negativa");
            } else if (saldo < cantidad) {
                System.out.println("La cantidad a retirar no puede ser superior al saldo existente");
            } else {
                saldo -= cantidad;
            }
        }
    }
