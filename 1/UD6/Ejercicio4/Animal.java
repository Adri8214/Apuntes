package UD6.Ejercicio4;

public class Animal {
    String nombre;
    String tipoAlimentacion;
    
    public Animal(String nombre, String tipoAlimentacion) {
        this.nombre = nombre;
        this.tipoAlimentacion = tipoAlimentacion;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + " | Tipo de alimentación: " + tipoAlimentacion;
    }
    
}
