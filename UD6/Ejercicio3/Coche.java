package UD6.Ejercicio3;

public class Coche extends Vehiculo {
    private int numeroPuertas;

    public Coche(String marca, String tipoCombustible, int numeroPuertas) {
        super(marca, tipoCombustible);
        this.numeroPuertas = numeroPuertas;
    }

    @Override
    public String toString() {
        return super.toString() + " | " + numeroPuertas +  " puertas";
    }
}
