package UD6.Ejercicio5;

public class Libro extends MaterialBibliografico {
    private int numPaginas;
    private String genero;

    public Libro(String titulo, String autor, int numPaginas, String genero) {
        super(titulo, autor);
        this.numPaginas = numPaginas;
        this.genero = genero;
    }

    @Override
    public String toString() {
        return "Libro: " + titulo + " por " + autor +
               ", Género: " + genero + ", Páginas: " + numPaginas;
    }
}
