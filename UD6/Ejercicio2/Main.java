package UD6.Ejercicio2;

public class Main {
    public static void main(String[] args) {
        Empleado e1 = new Empleado("Jose", 1200);
        Programador p1 = new Programador("Francis", 1500);
        Diseniador d1 = new Diseniador("Raúl", 1000);
        Gerente g1 = new Gerente("Matías", 2000);

        System.out.println(e1);

        System.out.println(p1);
        System.out.println(p1.calcularSueldo());
        
        System.out.println(d1);
        System.out.println(d1.calcularSueldo());
        
        System.out.println(g1);
        System.out.println(g1.calcularSueldo());
    }
}
