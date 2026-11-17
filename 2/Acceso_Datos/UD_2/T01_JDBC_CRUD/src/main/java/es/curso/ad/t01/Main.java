package es.curso.ad.t01;

import java.math.BigDecimal;
import java.sql.SQLException;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        ClubDao dao = new ClubDao();
        try {
            System.out.println("CLUBES INICIALES");
            for (Club club : dao.listar()) {
                System.out.println(club);
            }

            String nombreTemporal = "Club de prueba JDBC";
            int id = dao.insertar(nombreTemporal, "Granada", new BigDecimal("120.50"));
            System.out.println("Creado con ID " + id);
            System.out.println("Buscado: " + dao.buscar(id).orElseThrow());
            System.out.println("Actualizado: " + dao.cambiarCiudad(id, "Jaén"));
            System.out.println("Tras cambiar: " + dao.buscar(id).orElseThrow());

            System.out.println("\n--- PROBANDO listarPorCiudad ---");
            

            String ciudadPrueba = "Jaén";
            List<Club> clubesCiudad = dao.listarPorCiudad(ciudadPrueba);
            System.out.println("Clubes en " + ciudadPrueba + " (" + clubesCiudad.size() + "):");
            for (Club c : clubesCiudad) {
                System.out.println(" * " + c.nombre());
            }

            String ciudadInexistente = "CiudadFalsa123";
            List<Club> clubesVacia = dao.listarPorCiudad(ciudadInexistente);
            System.out.println("Clubes en " + ciudadInexistente + " (Total encontrados: " + clubesVacia.size() + ")");


            String ciudadComilla = "O'Higgins";
            List<Club> clubesComillasRes = dao.listarPorCiudad(ciudadComilla);
            System.out.println("Búsqueda con comillas simples ejecutada correctamente (Resultados: " + clubesComillasRes.size() + ")");

            System.out.println("\nBorrado: " + dao.borrar(id));
            System.out.println("¿Sigue existiendo? " + dao.buscar(id).isPresent());
            
        } catch (SQLException e) {
            System.err.println("Error de base de datos: " + e.getMessage());
        }
    }
}
