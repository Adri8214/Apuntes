package UD6.Ejercicio5;

public class Revista extends MaterialBibliografico{
    private int edicion;
    private String periodicidad;

    public Revista(String titulo, String autor, int edicion, String periodicidad) {
        super(titulo, autor);
        this.edicion = edicion;
        this.periodicidad = periodicidad;
    }

    @Override
    public String toString() {
        return "Revista: " + titulo + " por " + autor +
               ", Edición: " + edicion + ", Periodicidad: " + periodicidad;
    }
    
}
