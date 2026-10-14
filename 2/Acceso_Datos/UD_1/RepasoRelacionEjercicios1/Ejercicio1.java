import java.nio.file.Path;

public class Ejercicio1 {
    public static void main(String[] args) {
        Path ruta = Path.of("datos");
        Path clubes = ruta.resolve("clubes.txt");
        Path copias = ruta.resolve("copias");

        System.out.println("=== RUTAS RELATIVAS ===");
        
        System.out.println(ruta.toAbsolutePath());
        System.out.println(clubes.toAbsolutePath());
        System.out.println(copias.toAbsolutePath());
        
        
        System.out.println("=== RUTAS ABSOLUTAS ===");
        
        System.out.println(ruta);
        System.out.println(clubes);
        System.out.println(copias);
    }
}
