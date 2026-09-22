package UD6.Ejercicio3;

public class Moto extends Vehiculo {
    private int cilindrada;

    public Moto(String marca, String tipoCombustible, int cilindrada) {
        super(marca, tipoCombustible);
        this.cilindrada = cilindrada;
    }

    @Override
    public String toString() {
        return super.toString() + " | " + cilindrada + "cc";
    }
}
