package UD6.Ejercicio5;

public class Main {
    public static void main(String[] args) {
        MaterialBibliografico m1 = new MaterialBibliografico("Cuaderno", "Anónimo");
        Revista r1 = new Revista("As", "Pedro Pérez", 1, "Lunes");
        Libro l1 = new Libro("El retrato de Dorian Gray", "Oscar Wilde", 250, "Drama");

        System.out.println(m1);
        System.out.println(r1);
        System.out.println(l1);
    }
}
