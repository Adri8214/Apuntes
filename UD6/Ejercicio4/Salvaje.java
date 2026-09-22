package UD6.Ejercicio4;

public class Salvaje extends Animal{
    private String habitat;

    public Salvaje(String nombre, String tipoAlimentacion, String habitat) {
        super(nombre, tipoAlimentacion);
        this.habitat = habitat;
    }

    String cazar() {
        return "El animal salvaje " + nombre + " caza en su hábitat " + habitat +
               " y su alimentación es " + tipoAlimentacion;
    }
}
