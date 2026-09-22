package UD6.Ejercicio1;

public class Televisor extends Electrodomestico {
    private double tamanioPantalla;

    public Televisor(String marca, String modelo, double tamanioPantalla) {
        super(marca, modelo);
        this.tamanioPantalla = tamanioPantalla;
    }

    @Override
    public String toString() {
        return super.toString() + " con tamaño " + tamanioPantalla + " cm.";
    }
}
