package UD6.Ejercicio3;

public class Vehiculo {
    private String marca;
    private String tipoCombustible;

    public Vehiculo(String marca, String tipoCombustible) {
        this.marca = marca;
        this.tipoCombustible = tipoCombustible;
    }

    @Override
    public String toString() {
        return "Marca: " + marca + " | Tipo de Combustible: "  + tipoCombustible;
    }
}
