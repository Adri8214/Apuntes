package UD6.Ejercicio2;

public class Empleado {
    String nombre;
    double sueldoBase;

    public Empleado(String nombre, double sueldoBase) {
        this.nombre = nombre;
        this.sueldoBase = sueldoBase;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + " | Sueldo base: " + sueldoBase;
    }
}
