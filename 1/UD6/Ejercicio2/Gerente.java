package UD6.Ejercicio2;

public class Gerente extends Empleado {
    private final double BONIFICACION = 4;

    public Gerente(String nombre, double sueldoBase) {
        super(nombre, sueldoBase);
    }

    double calcularSueldo() {
        return sueldoBase + BONIFICACION;
    }

    @Override
    public String toString() {
        return super.toString() + " | Tiene una bonificación de: " + BONIFICACION + "€";
    }  
}
