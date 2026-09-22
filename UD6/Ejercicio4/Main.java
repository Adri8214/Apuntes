package UD6.Ejercicio4;

public class Main {
    public static void main(String[] args) {
        Animal a1 = new Animal("Simba", "Carnívora");
        Domestico d1 = new Domestico("Panky", "Omnívora", "Laura");
        Salvaje s1 = new Salvaje("León", "Cárnivora", "Sabana");

        System.out.println(a1);
        System.out.println(d1.convivirConHumanos());
        System.out.println(s1.cazar());
    }
}
