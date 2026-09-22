package UD6.Ejercicio3;

public class Main {
    public static void main(String[] args) {
        Vehiculo v1 = new Vehiculo("Mazda", "Diésel");
        Coche c1 = new Coche("Mercedes", "Gasolina", 5);
        Moto m1 = new Moto("KTM", "Diésel", 700);

        System.out.println(v1);
        System.out.println(c1);
        System.out.println(m1);
    }
}
