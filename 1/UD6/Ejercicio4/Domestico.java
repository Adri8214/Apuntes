package UD6.Ejercicio4;

public class Domestico extends Animal{
    private String duenio;

    public Domestico(String nombre, String tipoAlimentacion, String duenio) {
        super(nombre, tipoAlimentacion);
        this.duenio = duenio;
    }

    String convivirConHumanos() {
        return "El animal doméstico " + nombre + 
               " convive con su dueño/a " + duenio +
               " y su alimentación es " + tipoAlimentacion;
    }
}
