package UD6.Ejercicio1;

public class Main {
    public static void main(String[] args) {
        Electrodomestico e1 = new Electrodomestico("Bosch", "200Z-45");
        Lavadora l1 = new Lavadora("Fujitsu", "201A-23", 12.5);
        Televisor t1 = new Televisor("Sony", "202B-24", 65);
        
        System.out.println(e1);
        System.out.println(l1);
        System.out.println(t1);
    }
}
