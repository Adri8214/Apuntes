package UD6.Ejercicio2;

public class Diseniador extends Empleado{
    private final double BONIFICACION = 150;

    public Diseniador(String nombre, double sueldoBase) {
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
