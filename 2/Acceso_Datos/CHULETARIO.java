/*
======================================================================
CHULETARIO MAESTRO ACCESO A DATOS (UD1) - VERSIÓN 2 - JAVA 17+
======================================================================
CÓMO USARLO EN EL EXAMEN:
- Abre este archivo y busca con CTRL + F. Mira primero la TABLA
  "SI EL ENUNCIADO DICE..." de aquí abajo: te dice qué etiqueta buscar.
- Todo está en UN solo archivo para poder consultarlo. En el examen cada
  clase va en su propio .java. Copia el MÉTODO que necesites y ADÁPTALO.
- NO metas este archivo en la carpeta del examen (chocaría con tus clases).
- Compilar:  javac -encoding UTF-8 *.java      Ejecutar:  java Main
- PROHIBIDO RandomAccessFile. No uses nada que no esté en estos apuntes.

======================================================================
SI EL ENUNCIADO DICE...                        -> BUSCA (CTRL + F)
======================================================================
"cargar / leer el CSV / omite la cabecera"        -> CARGAR CSV
"guardar / reescribir el fichero / cabecera"      -> GUARDAR CSV
"buscar por ID / devuelve el objeto o null"       -> BUSCAR POR ID
"añadir / alta / rechaza ID repetido o vacío"     -> ALTA
"modificar stock / plazas / cambiar un campo"     -> MODIFICAR
"eliminar / baja / borrar"                        -> ELIMINAR
"informe / valor total / suma / más caro / stock
 bajo / media / contar / filtrar / ordenar"       -> INFORMES
"copia de seguridad / restaurar / .bak / fecha"   -> COPIAS
"binario / Serializable / .dat / ObjectOutputStream" -> BINARIO
"XML / DOM / exportar / importar / fusionar"      -> XML
"JSON / Jackson / ObjectMapper"                   -> JSON
"menú / submenú / opción / confirmación S/N"      -> MENU
"repositorio / interfaz / cambiar de TXT a binario" -> REPOSITORIO
"leer teclado / número / decimal / null"          -> FUNCIONES
"CSV sin objetos / solo líneas (Relación 2)"      -> CSV LINEAS
"importar CSV con filas erróneas / productos_errores" -> IMPORTADOR
"no encuentra datos / ruta / package / carpeta"   -> EJECUCIÓN
"escribir / añadir / leer un TXT (Relación 1)"    -> TEXTO
"crear carpeta / existe / tamaño / listar carpeta" -> ARCHIVOS

======================================================================
CÓMO ADAPTAR UN MÉTODO COPIADO (¡LEE ESTO ANTES DE COPIAR!)
======================================================================
Casi todos los fallos al copiar son RESTOS DEL EJEMPLO ANTIGUO. Repasa:
 1. CLASE del modelo: Inscripcion -> Producto -> Equipo...  (new X(...))
 2. CAMPOS: cuántos hay (length != 4), qué índice es cada uno
    (campos[2]...), y si es entero (parseInt) o decimal (parseDouble).
 3. GETTERS / SETTERS: getPlazas -> getStock, setPlazas -> setStock...
 4. RUTA: CSV / RUTA / DAT... y el nombre del fichero.
 5. MÉTODOS AUXILIARES que llama el código (buscarPorId...): ¿existen en
    TU clase y con esos parámetros? Si no, escribe un for.
 6. TIPO DE DEVOLUCIÓN que pide el enunciado: boolean / objeto o null /
    lista / excepción (IOException o IllegalArgumentException).
 7. VARIABLES que ya no existen (plazas, taller...): bórralas.
 8. Compila y lee el PRIMER error: casi siempre es un nombre viejo.
Las líneas marcadas con   // <<< ADAPTAR   son las que casi siempre cambian.

======================================================================
LO QUE MÁS SE OLVIDA (comprueba siempre)
======================================================================
 - El bucle de lectura empieza en i = 1 (se salta la CABECERA).
 - guardar() ESCRIBE LA CABECERA antes de los registros.
 - Antes de modificar/eliminar un fichero: crearCopia() (si hay cambio).
 - Si el ID no existe: NO copiar, NO reescribir, devolver false.
 - Validar ANTES de guardar: un dato inválido guardado rompe la siguiente carga.
 - Importar/cargar: validar TODO en una lista temporal y sustituir al final.
 - Main: texto en vez de número NO debe cerrar el programa (null / try-catch).
 - Ejecuta SIEMPRE desde la carpeta que contiene la carpeta "datos".

======================================================================
ETIQUETAS (CTRL + F):
 [BUSCAR: IMPORTS] [BUSCAR: API FILES] [BUSCAR: EJECUCIÓN] [BUSCAR: RUTAS]
 [BUSCAR: ARCHIVOS] [BUSCAR: TEXTO] [BUSCAR: FUNCIONES]
 --- CON OBJETOS Inscripcion (Relación 4 - Ej. 1) ---
 [BUSCAR: MODELO CSV] [BUSCAR: GESTOR CSV] [BUSCAR: GESTOR DIRECTO]
 [BUSCAR: MAIN CSV]
 --- CSV SIN OBJETOS (Relación 2) ---
 [BUSCAR: CSV LINEAS] [BUSCAR: IMPORTADOR]
 --- CON OBJETOS Equipo (Relación 4 - Ej. 2) ---
 [BUSCAR: MODELO BINARIO] [BUSCAR: BINARIO] [BUSCAR: XML EXPORTAR]
 [BUSCAR: XML IMPORTAR] [BUSCAR: MAIN BINARIO]
 --- INVENTARIO DE PRODUCTOS (id;nombre;precio;stock) ---
 [BUSCAR: PRODUCTO] [BUSCAR: INVENTARIO] [BUSCAR: INFORMES]
 [BUSCAR: CARGAR CSV PRODUCTOS] [BUSCAR: COPIAS] [BUSCAR: BINARIO PRODUCTOS]
 [BUSCAR: XML PRODUCTOS] [BUSCAR: MENU]
 --- OTROS ---
 [BUSCAR: JSON] [BUSCAR: REPOSITORIO] [BUSCAR: ERRORES]
======================================================================
*/

// ====================================================================
// [BUSCAR: IMPORTS] - COPIA ESTE BLOQUE AL PRINCIPIO DE CADA .java
// (borra los que no uses; si te da igual, usa los comodines)
// ====================================================================
// ATAJO:  import java.io.*;  import java.nio.file.*;  import java.util.*;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.nio.charset.StandardCharsets;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.nio.file.StandardOpenOption;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

/*
======================================================================
[BUSCAR: API FILES] - RESUMEN RÁPIDO (qué hace cada cosa)
======================================================================
Path.of("datos")                  -> construye una ruta (NO crea nada)
carpeta.resolve("a.txt")          -> datos/a.txt
ruta.toAbsolutePath()             -> ruta absoluta (no comprueba que exista)
ruta.getParent() / getFileName()  -> carpeta contenedora / solo el nombre

Files.exists(ruta) / notExists    -> ¿existe? (notExists NO es siempre !exists)
Files.createDirectories(carpeta)  -> crea carpeta y padres; no falla si ya existe
Files.createFile(ruta)            -> crea vacío; FALLA si ya existe
Files.size(ruta)                  -> bytes
Files.isRegularFile(ruta)         -> ¿archivo normal (no carpeta)?
Files.deleteIfExists(ruta)        -> borra si existe (IRREVERSIBLE: pide confirmación)
Files.copy(o, d, REPLACE_EXISTING)-> copia (si no pones la opción y existe, falla)
Files.readAllLines(ruta, UTF_8)   -> List<String> con todas las líneas
Files.write(ruta, lista, UTF_8)   -> escribe líneas SUSTITUYENDO el contenido
Files.newBufferedWriter(...)      -> escritor (sustituye; con CREATE+APPEND añade)
Files.newBufferedReader(...)      -> lector; readLine() devuelve null al final
Files.newOutputStream / newInputStream -> flujos de bytes para objetos serializados

linea.split(";", -1)              -> campos (el -1 conserva los vacíos del final)
Integer.parseInt(texto)           -> lanza NumberFormatException si no es número
texto.trim() / isEmpty() / isBlank() / equalsIgnoreCase(otro)
======================================================================
*/

/*
======================================================================
[BUSCAR: EJECUCIÓN] - "NO ENCUENTRA LA CARPETA datos" / PACKAGE / IDE
======================================================================
- Las rutas Path.of("datos", ...) son RELATIVAS: se buscan desde la carpeta
  desde la que EJECUTAS el programa. Si "datos" está en otro sitio, el
  programa no la encuentra (en VS Code: File > Open Folder y abre la carpeta
  que contiene a la vez los .java y la carpeta datos).
- En IntelliJ/Eclipse: datos va en la RAÍZ del proyecto (junto a src).
- Si los archivos empiezan con "package xxx;" y compilas con javac a mano
  desde la propia carpeta, BORRA esa línea (o compila desde la carpeta raíz).
- Para comprobar dónde estás:  System.out.println(Path.of("").toAbsolutePath());
- Quita los comentarios raros que pueda haber (p. ej. "[cite: 12]").
======================================================================
*/

// ====================================================================
// [BUSCAR: RUTAS] - Relación 1, ejercicio 1
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- Construir o mostrar una ruta NO crea ningún archivo.
- Una ruta relativa se interpreta desde donde EJECUTAS el programa.
*/
class SeccionRutas {
    static void ejemplo() {
        Path carpeta = Path.of("datos");                      // datos
        Path archivo = carpeta.resolve("clubes.txt");         // datos/clubes.txt
        Path copias = carpeta.resolve("copias");              // datos/copias
        Path bak = Path.of("datos", "copias", "clubes.bak");  // varias partes de golpe

        System.out.println("Relativa: " + archivo);
        System.out.println("Absoluta: " + archivo.toAbsolutePath());
        System.out.println("Padre:    " + archivo.getParent());    // datos
        System.out.println("Nombre:   " + archivo.getFileName());  // clubes.txt
        System.out.println(copias + " | " + bak);
    }
}

// ====================================================================
// [BUSCAR: ARCHIVOS] - Relación 1, ejercicios 2, 3 y 4
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- createDirectories ANTES de escribir en una carpeta que puede no existir.
- createFile solo si notExists, para no fallar ni sobrescribir.
- Borrar es irreversible: pide confirmación en Main antes de llamar a borrar().
*/
class SeccionArchivos {

    // Ej. 2: crear carpetas y archivos vacíos SIN sobrescribir lo existente
    static void prepararCarpetas() throws IOException {
        Path datos = Path.of("datos");
        Path copias = datos.resolve("copias");
        Path clubes = datos.resolve("clubes.txt");
        Path respaldo = copias.resolve("respaldo.txt");

        Files.createDirectories(copias);  // crea datos y datos/copias
        if (Files.notExists(clubes)) {
            Files.createFile(clubes);
        }
        if (Files.notExists(respaldo)) {
            Files.createFile(respaldo);
        }
        for (Path p : List.of(clubes, respaldo)) {
            System.out.println(p + " | existe: " + Files.exists(p)
                    + " | tamaño: " + Files.size(p) + " bytes");
        }
    }

    // Ej. 3: inspector de un fichero (no debe cerrarse si falla)
    static void inspeccionar(Path archivo) {
        System.out.println("Ruta absoluta: " + archivo.toAbsolutePath());
        if (Files.notExists(archivo)) {
            System.out.println("El archivo no existe.");
            return;
        }
        try {
            System.out.println("Tamaño: " + Files.size(archivo) + " bytes");
        } catch (IOException e) {
            System.err.println("No se pudo acceder al archivo: " + e.getMessage());
        }
    }

    // Ej. 4: listar SOLO los archivos (no subcarpetas) de una carpeta
    static void listarArchivos(Path carpeta) {
        if (Files.notExists(carpeta)) {
            System.out.println("La carpeta " + carpeta + " no existe.");
            return;
        }
        // try-with-resources: cierra el DirectoryStream automáticamente
        try (DirectoryStream<Path> elementos = Files.newDirectoryStream(carpeta)) {
            for (Path elemento : elementos) {
                if (Files.isRegularFile(elemento)) {
                    System.out.println(elemento.getFileName());  // solo el nombre
                }
            }
        } catch (IOException e) {
            System.err.println("No se pudo listar: " + e.getMessage());
        }
    }

    // Borrar un archivo (devuelve true si existía y se borró)
    static boolean borrar(Path archivo) throws IOException {
        return Files.deleteIfExists(archivo);
    }
}

// ====================================================================
// [BUSCAR: TEXTO] - Relación 1, ejercicios 5, 6, 7 y 8
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- newBufferedWriter(ruta, UTF_8)                  -> SUSTITUYE el contenido.
- newBufferedWriter(ruta, UTF_8, CREATE, APPEND)  -> AÑADE al final (crea si falta).
- Siempre try-with-resources y UTF-8 explícito.
- APPEND no comprueba duplicados: eso lo haces tú (ver GESTOR CSV / CSV LINEAS).
- Si el fichero no acaba en salto de línea, la línea nueva se pega a la última.
*/
class SeccionTexto {
    static final Path RUTA = Path.of("datos", "clubes.txt");

    // Ej. 5: escribir sustituyendo (cada ejecución deja SOLO estas 3 líneas)
    static void guardarClubes() throws IOException {
        Files.createDirectories(RUTA.getParent());
        try (BufferedWriter salida = Files.newBufferedWriter(RUTA, StandardCharsets.UTF_8)) {
            salida.write("1;Granada CF;Granada");
            salida.newLine();
            salida.write("2;Málaga CF;Málaga");
            salida.newLine();
            salida.write("3;Cádiz CF;Cádiz");
            salida.newLine();
        }
    }

    // Ej. 7: añadir una línea al final conservando lo anterior
    static void anadirLinea(String linea) throws IOException {
        Files.createDirectories(RUTA.getParent());
        try (BufferedWriter salida = Files.newBufferedWriter(RUTA, StandardCharsets.UTF_8,
                StandardOpenOption.CREATE, StandardOpenOption.APPEND)) {
            salida.write(linea);
            salida.newLine();
        }
    }

    // Ej. 6: leer línea a línea con BufferedReader (readLine devuelve null al final)
    static void mostrarLineas() throws IOException {
        if (Files.notExists(RUTA)) {
            System.out.println("Todavía no hay un archivo de clubes.");
            return;
        }
        try (BufferedReader entrada = Files.newBufferedReader(RUTA, StandardCharsets.UTF_8)) {
            String linea;
            while ((linea = entrada.readLine()) != null) {
                System.out.println(linea);
            }
        }
    }

    // Leer todo de golpe y contar registros (sin contar líneas vacías)
    static int contarRegistros() throws IOException {
        List<String> lineas = Files.readAllLines(RUTA, StandardCharsets.UTF_8);
        int total = 0;
        for (String linea : lineas) {
            if (!linea.isBlank()) {
                total++;
            }
        }
        return total;
    }

    // Escribir una lista de líneas de golpe (sustituye el contenido)
    static void guardarLineas(List<String> lineas) throws IOException {
        Files.write(RUTA, lineas, StandardCharsets.UTF_8);
    }

    // Ej. 8: pedir por teclado, añadir y volver a mostrar todo
    static void registroClubes() {
        Scanner teclado = new Scanner(System.in);
        System.out.print("ID: ");
        String id = teclado.nextLine().trim();
        System.out.print("Nombre: ");
        String nombre = teclado.nextLine().trim();
        System.out.print("Ciudad: ");
        String ciudad = teclado.nextLine().trim();
        try {
            anadirLinea(id + ";" + nombre + ";" + ciudad);
            mostrarLineas();
        } catch (IOException e) {
            System.err.println("Error de entrada/salida: " + e.getMessage());
        }
    }
}

// ====================================================================
// [BUSCAR: FUNCIONES] - AYUDAS PARA MAIN (tu Funciones.java ampliado)
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- Si el examen te da una clase de ayuda, úsala. Si no, copia estas.
- leerEntero devuelve Integer: null significa "no escribió un número".
  En Main: if (valor == null) { mensaje de error } else { ... }
- Estas ayudas SÍ leen teclado/imprimen porque se llaman desde Main;
  GestorInscripciones y RepositorioEquipos NO deben hacerlo.
*/
class Funciones {

    static Integer leerEntero(Scanner teclado, String mensaje) {
        System.out.print(mensaje);
        String entrada = teclado.nextLine();
        Integer numero;
        try {
            numero = Integer.valueOf(entrada.trim());
        } catch (NumberFormatException e) {
            numero = null;
        }
        return numero;
    }

    // Decimal: acepta coma o punto. Devuelve null si NO es un número.
    static Double leerDecimal(Scanner teclado, String mensaje) {
        System.out.print(mensaje);
        String entrada = teclado.nextLine().trim().replace(',', '.');
        try {
            return Double.valueOf(entrada);
        } catch (NumberFormatException e) {
            return null;
        }
    }

    // ¿El texto es un entero? (para validar sin try/catch en cada sitio)
    static boolean esEntero(String texto) {
        try {
            Integer.parseInt(texto.trim());
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    static String leerTexto(Scanner teclado, String mensaje) {
        System.out.print(mensaje);
        return teclado.nextLine().trim();
    }

    // Confirmación S/N: true solo si escribe S o s
    static boolean confirmar(Scanner teclado, String mensaje) {
        String respuesta = leerTexto(teclado, mensaje + " (S/N): ");
        return respuesta.equalsIgnoreCase("S");
    }

    static boolean existeArchivo(Path archivo) {
        boolean existe = Files.exists(archivo);
        if (!existe) {
            System.out.println("No existe el archivo: " + archivo);
        }
        return existe;
    }

    static void crearCarpetaSiNoExiste(Path carpeta) throws IOException {
        if (!Files.exists(carpeta)) {
            Files.createDirectories(carpeta);
        }
    }

    // Copia de seguridad (una sola copia: la siguiente la sustituye)
    static void crearCopiaSeguridad(Path archivo, Path carpetaCopias, Path copia)
            throws IOException {
        crearCarpetaSiNoExiste(carpetaCopias);
        Files.copy(archivo, copia, StandardCopyOption.REPLACE_EXISTING);
    }

    // Variante: copia con fecha y hora en el nombre (conserva varias copias)
    static Path crearCopiaConFecha(Path archivo, Path carpetaCopias) throws IOException {
        crearCarpetaSiNoExiste(carpetaCopias);
        String marca = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMdd_HHmmss"));
        Path destino = carpetaCopias.resolve(archivo.getFileName() + "_" + marca + ".bak");
        Files.copy(archivo, destino, StandardCopyOption.REPLACE_EXISTING);
        return destino;
    }
}

// ====================================================================
// [BUSCAR: MODELO CSV] - Inscripcion (RELACIÓN 4 - EJ. 1)
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- Esta clase ya te la dan resuelta. Aquí para ver qué getters/métodos tiene.
- Formato del CSV: id;persona;taller;plazas  (con cabecera en la 1.ª línea).
*/
class Inscripcion {
    private final int id;
    private final String persona;
    private final String taller;
    private int plazas;

    Inscripcion(int id, String persona, String taller, int plazas) {
        this.id = id;
        this.persona = persona;
        this.taller = taller;
        this.plazas = plazas;
    }

    int getId() { return id; }
    String getPersona() { return persona; }
    String getTaller() { return taller; }
    int getPlazas() { return plazas; }
    void setPlazas(int plazas) { this.plazas = plazas; }

    // Línea tal y como se guarda en el CSV
    String toCsv() {
        return id + ";" + persona + ";" + taller + ";" + plazas;
    }

    @Override
    public String toString() {
        return id + " | " + persona + " | " + taller + " | plazas: " + plazas;
    }
}

// ====================================================================
// [BUSCAR: GESTOR CSV] - GestorInscripciones (RELACIÓN 4 - EJ. 1)
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN (orden del enunciado):
 TODO 1.1 cargar()          -> lee, valida y construye la lista
 TODO 1.2 buscarPorId()     -> devuelve el objeto o null
 TODO 1.3 modificarPlazas() -> rechaza plazas < 0 o ID inexistente; copia + guardar
 TODO 1.4 eliminar()        -> si no aparece: NO copia y NO reescribe
 TODO 1.5 restaurar()       -> boolean; la confirmación S/N se pide en Main
 (guardar, anadir y crearCopia suelen venir ya resueltos: aquí por si acaso)

PATRÓN DE TODA MODIFICACIÓN EN TEXTO:
  leer todo -> cambiar EN MEMORIA -> (copia) -> reescribir TODO el fichero
  y solo si hubo cambio real (bandera boolean).
- Los errores de datos se lanzan como IOException (lo pide el enunciado) y
  Main los captura y muestra con e.getMessage().
- NADA de System.out ni Scanner aquí.
- Ajusta las rutas (CSV / COPIA) a las que diga el enunciado.
*/
class GestorInscripciones {
    static final Path CARPETA = Path.of("datos");
    static final Path CSV = CARPETA.resolve("inscripciones.csv");   // <<< ADAPTAR
    static final Path COPIA = CARPETA.resolve("inscripciones.csv.bak");
    static final String CABECERA = "id;persona;taller;plazas";

    // ---------- TODO 1.1: CARGAR EL CSV ----------
    // Omite la cabecera, split(";", -1), convierte ID y plazas, rechaza filas
    // inválidas o IDs repetidos lanzando IOException.
    static List<Inscripcion> cargar() throws IOException {
        List<Inscripcion> lista = new ArrayList<>();
        // Si el enunciado dice "si no existe, lista vacía", descomenta:
        // if (Files.notExists(CSV)) { return lista; }

        List<String> lineas = Files.readAllLines(CSV, StandardCharsets.UTF_8);
        for (int i = 1; i < lineas.size(); i++) {      // i = 1 -> se salta la cabecera
            String linea = lineas.get(i);
            if (linea.isBlank()) {
                continue;                              // ignora líneas vacías
            }
            String[] campos = linea.split(";", -1);
            if (campos.length != 4) {                       // <<< ADAPTAR (nº de campos)
                throw new IOException("Línea " + (i + 1) + ": se esperaban 4 campos");
            }
            int id;
            int plazas;
            try {
                id = Integer.parseInt(campos[0].trim());
                plazas = Integer.parseInt(campos[3].trim());
            } catch (NumberFormatException e) {
                throw new IOException("Línea " + (i + 1) + ": ID o plazas no son números", e);
            }
            String persona = campos[1].trim();
            String taller = campos[2].trim();
            if (id <= 0 || plazas < 0 || persona.isEmpty() || taller.isEmpty()) {
                throw new IOException("Línea " + (i + 1) + ": datos no válidos");
            }
            if (buscarPorId(lista, id) != null) {
                throw new IOException("Línea " + (i + 1) + ": ID repetido (" + id + ")");
            }
            lista.add(new Inscripcion(id, persona, taller, plazas));   // <<< ADAPTAR (clase y campos)
        }
        return lista;
    }

    // ---------- TODO 1.2: BUSCAR POR ID ----------
    static Inscripcion buscarPorId(List<Inscripcion> lista, int id) {
        for (Inscripcion inscripcion : lista) {
            if (inscripcion.getId() == id) {
                return inscripcion;
            }
        }
        return null;                                   // no encontrado
    }

    // ---------- GUARDAR (suele venir resuelto): cabecera + todos los registros ----------
    static void guardar(List<Inscripcion> lista) throws IOException {
        Files.createDirectories(CARPETA);
        List<String> lineas = new ArrayList<>();
        lineas.add(CABECERA);
        for (Inscripcion inscripcion : lista) {
            lineas.add(inscripcion.toCsv());
        }
        Files.write(CSV, lineas, StandardCharsets.UTF_8);   // sustituye el contenido
    }

    // ---------- COPIA (suele venir resuelta) ----------
    static void crearCopia() throws IOException {
        if (Files.exists(CSV)) {
            Files.createDirectories(CARPETA);
            Files.copy(CSV, COPIA, StandardCopyOption.REPLACE_EXISTING);
        }
    }

    // ---------- ALTA (opción 3, suele venir resuelta) ----------
    static boolean anadir(List<Inscripcion> lista, Inscripcion nueva) throws IOException {
        if (buscarPorId(lista, nueva.getId()) != null) {
            return false;                              // ID repetido: no se añade
        }
        lista.add(nueva);
        guardar(lista);
        return true;
    }

    // ---------- TODO 1.3: MODIFICAR PLAZAS ----------
    // false si plazas < 0 o el ID no existe (y entonces NO se toca el fichero).
    static boolean modificarPlazas(List<Inscripcion> lista, int id, int nuevasPlazas)
            throws IOException {
        if (nuevasPlazas < 0) {
            return false;
        }
        Inscripcion inscripcion = buscarPorId(lista, id);
        if (inscripcion == null) {
            return false;
        }
        crearCopia();                                  // copia ANTES de reescribir
        inscripcion.setPlazas(nuevasPlazas);           // cambio en memoria (solo ese registro)
        guardar(lista);                                // reescribe todos los registros
        return true;
    }

    // ---------- TODO 1.4: ELIMINAR ----------
    // Construye una lista nueva sin el ID. Si no aparece: no copia ni reescribe.
    static boolean eliminar(List<Inscripcion> lista, int id) throws IOException {
        List<Inscripcion> restantes = new ArrayList<>();
        boolean encontrado = false;
        for (Inscripcion inscripcion : lista) {
            if (inscripcion.getId() == id) {
                encontrado = true;                     // este NO se copia a la lista nueva
            } else {
                restantes.add(inscripcion);
            }
        }
        if (!encontrado) {
            return false;
        }
        crearCopia();
        guardar(restantes);
        lista.clear();                                 // deja la lista de Main igual que el fichero
        lista.addAll(restantes);
        return true;
    }

    // ---------- TODO 1.5: RESTAURAR ----------
    // true si había copia y se restauró. DESPUÉS Main debe volver a llamar a cargar().
    static boolean restaurar() throws IOException {
        if (Files.notExists(COPIA)) {
            return false;
        }
        Files.copy(COPIA, CSV, StandardCopyOption.REPLACE_EXISTING);
        return true;
    }

    // Para que Main pueda preguntar si hay copia SIN usar Files
    static boolean hayCopia() {
        return Files.exists(COPIA);
    }

    // Variante más segura (apartado 5 de la unidad): guarda antes lo que se va a pisar
    static boolean restaurarConservandoActual() throws IOException {
        if (Files.notExists(COPIA)) {
            return false;
        }
        if (Files.exists(CSV)) {
            Files.copy(CSV, CARPETA.resolve("inscripciones.csv.antes"),
                    StandardCopyOption.REPLACE_EXISTING);
        }
        Files.copy(COPIA, CSV, StandardCopyOption.REPLACE_EXISTING);
        return true;
    }
}

// ====================================================================
// [BUSCAR: CSV LINEAS] - CRUD EN CSV SIN OBJETOS (RELACIÓN 2)
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- Se trabaja con List<String> y split. La cabecera es la línea 0.
- Para modificar o borrar: lista nueva + bandera "encontrado" + escribir
  SOLO si encontrado. Todas las demás líneas se copian sin tocar.
- Errores de validación: IllegalArgumentException (o un String de motivo).
*/
class CsvPorLineas {
    // Ej. 1: mostrar cada registro con otro formato: [101] Hollow Knight - PC
    static void mostrarVideojuegos(Path archivo) throws IOException {
        List<String> lineas = Files.readAllLines(archivo, StandardCharsets.UTF_8);
        for (int i = 1; i < lineas.size(); i++) {              // salta cabecera
            String[] c = lineas.get(i).split(";", -1);
            if (c.length != 3) {
                System.out.println("Línea " + (i + 1) + " ignorada: no tiene 3 campos");
                continue;
            }
            try {
                int id = Integer.parseInt(c[0].trim());
                System.out.println("[" + id + "] " + c[1].trim() + " - " + c[2].trim());
            } catch (NumberFormatException e) {
                System.out.println("Línea " + (i + 1) + " ignorada: el ID '" + c[0] + "' no es número");
            }
        }
    }

    // Ej. 2: buscar por ID distinguiendo "no numérico" de "no existe"
    static String buscarAlumno(Path archivo, String idTexto) throws IOException {
        int buscado;
        try {
            buscado = Integer.parseInt(idTexto.trim());
        } catch (NumberFormatException e) {
            return "El ID '" + idTexto + "' no es un número.";
        }
        List<String> lineas = Files.readAllLines(archivo, StandardCharsets.UTF_8);
        for (int i = 1; i < lineas.size(); i++) {
            String[] c = lineas.get(i).split(";", -1);
            if (c.length == 3 && c[0].trim().equals(String.valueOf(buscado))) {
                return "Alumno: " + c[1] + " | Grupo: " + c[2];
            }
        }
        return "No existe ningún alumno con ID " + buscado + ".";
    }

    // Ej. 3: actualizar stock sin perder registros (formato id;nombre;stock)
    static boolean actualizarStock(Path archivo, int id, int nuevoStock) throws IOException {
        if (nuevoStock < 0 || Files.notExists(archivo)) {
            return false;
        }
        List<String> originales = Files.readAllLines(archivo, StandardCharsets.UTF_8);
        List<String> nuevas = new ArrayList<>();
        boolean encontrado = false;
        for (int i = 0; i < originales.size(); i++) {
            String linea = originales.get(i);
            if (i == 0) {                                       // cabecera: sin cambios
                nuevas.add(linea);
                continue;
            }
            String[] c = linea.split(";", -1);
            if (c.length != 3) {                                // registro raro: se conserva igual
                nuevas.add(linea);
                continue;
            }
            try {
                if (Integer.parseInt(c[0].trim()) == id) {
                    nuevas.add(c[0] + ";" + c[1] + ";" + nuevoStock);  // SOLO este cambia
                    encontrado = true;
                } else {
                    nuevas.add(linea);
                }
            } catch (NumberFormatException e) {
                nuevas.add(linea);
            }
        }
        if (!encontrado) {
            return false;                                       // ID inexistente: no reescribir
        }
        Files.write(archivo, nuevas, StandardCharsets.UTF_8);
        return true;
    }

    // Ej. 4: cancelar reserva (borrar por reconstrucción), conserva cabecera
    static boolean cancelarReserva(Path archivo, int id) throws IOException {
        List<String> originales = Files.readAllLines(archivo, StandardCharsets.UTF_8);
        List<String> nuevas = new ArrayList<>();
        boolean encontrado = false;
        for (int i = 0; i < originales.size(); i++) {
            String linea = originales.get(i);
            if (i == 0) {
                nuevas.add(linea);
                continue;
            }
            String[] c = linea.split(";", -1);
            if (c.length == 3 && c[0].trim().equals(String.valueOf(id))) {
                encontrado = true;                              // no se añade -> desaparece
            } else {
                nuevas.add(linea);
            }
        }
        if (!encontrado) {
            return false;
        }
        Files.write(archivo, nuevas, StandardCharsets.UTF_8);
        return true;
    }

    // Ej. 5: alta sin duplicados (ID y título ignorando mayúsculas/espacios)
    // Lanza IllegalArgumentException con el motivo si algo no vale.
    static void anadirLibro(Path archivo, String idTexto, String titulo, String autor)
            throws IOException {
        int id;
        try {
            id = Integer.parseInt(idTexto.trim());
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("El ID no es numérico");
        }
        if (id <= 0) {
            throw new IllegalArgumentException("El ID debe ser mayor que 0");
        }
        titulo = titulo.trim();
        autor = autor.trim();
        if (titulo.isEmpty() || autor.isEmpty()) {
            throw new IllegalArgumentException("Título y autor no pueden estar vacíos");
        }
        if (Files.exists(archivo)) {
            List<String> lineas = Files.readAllLines(archivo, StandardCharsets.UTF_8);
            for (int i = 1; i < lineas.size(); i++) {
                String[] c = lineas.get(i).split(";", -1);
                if (c.length != 3) {
                    continue;
                }
                if (c[0].trim().equals(String.valueOf(id))) {
                    throw new IllegalArgumentException("ID repetido: " + id);
                }
                if (c[1].trim().equalsIgnoreCase(titulo)) {
                    throw new IllegalArgumentException("Título repetido: " + c[1].trim());
                }
            }
        }
        // Solo si TODO es válido: añadir al final
        try (BufferedWriter salida = Files.newBufferedWriter(archivo, StandardCharsets.UTF_8,
                StandardOpenOption.CREATE, StandardOpenOption.APPEND)) {
            salida.write(id + ";" + titulo + ";" + autor);
            salida.newLine();
        }
    }

    // Ej. 7: editar con red de seguridad (copia -> modificar) y restaurar
    static boolean actualizarStockConCopia(Path archivo, Path copia, int id, int nuevoStock)
            throws IOException {
        if (Files.notExists(archivo)) {
            return false;
        }
        Funciones.crearCopiaSeguridad(archivo, copia.getParent(), copia);
        return actualizarStock(archivo, id, nuevoStock);
    }

    // Restaurar: false si no hay copia (y se conserva el archivo actual)
    static boolean restaurarCopia(Path archivo, Path copia) throws IOException {
        if (Files.notExists(copia)) {
            return false;
        }
        Files.copy(copia, archivo, StandardCopyOption.REPLACE_EXISTING);
        return true;
    }

    // Ej. 8 (gestor de préstamos): NO hay código nuevo. Combina lo anterior:
    //  alta = anadirLibro (validar + APPEND) | baja = cancelarReserva |
    //  cambio = actualizarStock | listado = mostrarVideojuegos | copia = crearCopiaSeguridad
    //  Antes de cada reescritura -> crearCopiaSeguridad(prestamos.csv -> prestamos.bak).
    //  Si prestamos.csv no existe al iniciar: tratarlo como lista vacía (Files.notExists).
}

// ====================================================================
// [BUSCAR: IMPORTADOR] - RELACIÓN 2, EJ. 6 (productos_errores.csv)
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- Por cada fila mala: guardar "Línea N: motivo" y CONTINUAR (continue).
- Nunca se sobrescribe el fichero de entrada: se escribe uno NUEVO.
- Número de línea real = i + 1 (porque i empieza en 0 y hay cabecera).
- Main imprime la lista "errores" que se devuelve rellenada.
*/
class ImportadorProductos {
    static int importar(Path entrada, Path salida, List<String> errores) throws IOException {
        List<String> lineas = Files.readAllLines(entrada, StandardCharsets.UTF_8);
        List<String> validas = new ArrayList<>();
        List<Integer> idsAceptados = new ArrayList<>();
        validas.add("id;nombre;stock");                         // cabecera del fichero nuevo

        for (int i = 1; i < lineas.size(); i++) {
            int numLinea = i + 1;
            String linea = lineas.get(i);
            if (linea.isBlank()) {
                continue;
            }
            String[] c = linea.split(";", -1);
            if (c.length != 3) {
                errores.add("Línea " + numLinea + ": no tiene 3 campos");
                continue;
            }
            int id;
            int stock;
            try {
                id = Integer.parseInt(c[0].trim());
                stock = Integer.parseInt(c[2].trim());
            } catch (NumberFormatException e) {
                errores.add("Línea " + numLinea + ": ID o stock no numérico");
                continue;
            }
            String nombre = c[1].trim();
            if (id <= 0) {
                errores.add("Línea " + numLinea + ": el ID debe ser positivo");
            } else if (nombre.isEmpty()) {
                errores.add("Línea " + numLinea + ": nombre vacío");
            } else if (stock < 0) {
                errores.add("Línea " + numLinea + ": stock negativo");
            } else if (idsAceptados.contains(id)) {
                errores.add("Línea " + numLinea + ": ID duplicado (" + id + ")");
            } else {
                idsAceptados.add(id);
                validas.add(id + ";" + nombre + ";" + stock);
            }
        }
        Files.write(salida, validas, StandardCharsets.UTF_8);
        return validas.size() - 1;                              // cuántas válidas (sin cabecera)
    }
}

// ====================================================================
// [BUSCAR: MODELO BINARIO] - Equipo (RELACIÓN 4 - EJ. 2)
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- Para serializar: implements Serializable + serialVersionUID.
- Si cambias los campos de la clase, los .dat antiguos pueden dejar de leerse.
*/
class Equipo implements Serializable {
    private static final long serialVersionUID = 1L;

    private final int id;
    private final String nombre;
    private int unidades;

    Equipo(int id, String nombre, int unidades) {
        this.id = id;
        this.nombre = nombre;
        this.unidades = unidades;
    }

    int getId() { return id; }
    String getNombre() { return nombre; }
    int getUnidades() { return unidades; }
    void setUnidades(int unidades) { this.unidades = unidades; }

    @Override
    public String toString() {
        return id + " | " + nombre + " | unidades: " + unidades;
    }
}

// ====================================================================
// [BUSCAR: BINARIO] [BUSCAR: XML EXPORTAR] [BUSCAR: XML IMPORTAR]
// RepositorioEquipos (RELACIÓN 4 - EJ. 2)
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN (orden del enunciado):
 TODO 2.1 cargar()          -> .dat no existe = lista vacía; si existe: readObject,
                               instanceof List<?>, instanceof Equipo, sin IDs repetidos
 TODO 2.2 guardar()         -> crear carpeta + ObjectOutputStream, SIN APPEND
 TODO 2.3 cambiarUnidades() -> SOLO en memoria (no guardar aquí)
 TODO 2.4 exportarXml()     -> raíz <equipos>, <equipo id=".."><nombre/><unidades/>

- Se guarda la LISTA ENTERA como un único objeto (nunca varios writeObject
  con APPEND: cada apertura escribe una cabecera nueva y se corrompe).
- ClassNotFoundException e IOException del XML se envuelven en IOException
  para que la firma sea "throws IOException" y Main solo capture eso.
- NO deserializar ficheros de origen desconocido.
*/
class RepositorioEquipos {
    static final Path DAT = Path.of("datos", "equipos.dat");   // <<< ADAPTAR
    static final Path XML = Path.of("datos", "equipos.xml");

    // ---------- TODO 2.1: CARGAR LISTA BINARIA ----------
    static List<Equipo> cargar() throws IOException {
        List<Equipo> equipos = new ArrayList<>();
        if (Files.notExists(DAT)) {
            return equipos;                                     // sin fichero -> lista vacía
        }
        try (ObjectInputStream entrada = new ObjectInputStream(Files.newInputStream(DAT))) {
            Object dato = entrada.readObject();                 // se lee como Object
            if (!(dato instanceof List<?> lista)) {
                throw new IOException("El archivo no contiene una lista");
            }
            for (Object elemento : lista) {
                if (!(elemento instanceof Equipo equipo)) {      // <<< ADAPTAR (clase)
                    throw new IOException("La lista contiene un elemento que no es un Equipo");
                }
                if (buscarPorId(equipos, equipo.getId()) != null) {
                    throw new IOException("ID duplicado en el archivo: " + equipo.getId());
                }
                equipos.add(equipo);
            }
        } catch (ClassNotFoundException ex) {
            throw new IOException("No se encuentra la clase del objeto guardado", ex);
        }
        return equipos;
    }

    // ---------- TODO 2.2: GUARDAR LISTA BINARIA ----------
    static void guardar(List<Equipo> equipos) throws IOException {
        Files.createDirectories(DAT.getParent());               // crea datos si falta
        // newOutputStream por defecto SUSTITUYE el fichero (no usar APPEND)
        try (ObjectOutputStream salida = new ObjectOutputStream(Files.newOutputStream(DAT))) {
            salida.writeObject(new ArrayList<>(equipos));       // lista completa de una vez
        }
    }

    // ---------- Búsqueda por ID (ya resuelta en el examen) ----------
    static Equipo buscarPorId(List<Equipo> equipos, int id) {
        for (Equipo equipo : equipos) {
            if (equipo.getId() == id) {
                return equipo;
            }
        }
        return null;
    }

    // ---------- TODO 2.3: CAMBIAR UNIDADES (solo en memoria) ----------
    static boolean cambiarUnidades(List<Equipo> equipos, int id, int nuevasUnidades) {
        if (nuevasUnidades < 0) {
            return false;                                       // unidades no válidas
        }
        Equipo equipo = buscarPorId(equipos, id);
        if (equipo == null) {
            return false;                                       // ID inexistente
        }
        equipo.setUnidades(nuevasUnidades);                     // NO se guarda aquí
        return true;
    }

    // ---------- TODO 2.4: EXPORTAR A XML CON DOM ----------
    static void exportarXml(List<Equipo> equipos) throws IOException {
        exportarXml(equipos, XML);
    }

    static void exportarXml(List<Equipo> equipos, Path destino) throws IOException {
        try {
            // 1) Documento vacío y raíz <equipos>
            Document documento = DocumentBuilderFactory.newInstance()
                    .newDocumentBuilder().newDocument();
            Element raiz = documento.createElement("equipos");
            documento.appendChild(raiz);

            // 2) Un <equipo id="..."> por objeto, con hijos <nombre> y <unidades>
            for (Equipo equipo : equipos) {
                Element elemento = documento.createElement("equipo");
                elemento.setAttribute("id", String.valueOf(equipo.getId()));

                Element nombre = documento.createElement("nombre");
                nombre.setTextContent(equipo.getNombre());      // DOM escapa & como &amp;
                Element unidades = documento.createElement("unidades");
                unidades.setTextContent(String.valueOf(equipo.getUnidades()));

                elemento.appendChild(nombre);
                elemento.appendChild(unidades);
                raiz.appendChild(elemento);
            }

            // 3) Escribir el fichero con Transformer (UTF-8 + indentación)
            if (destino.getParent() != null) {
                Files.createDirectories(destino.getParent());
            }
            Transformer transformador = TransformerFactory.newInstance().newTransformer();
            transformador.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
            transformador.setOutputProperty(OutputKeys.INDENT, "yes");
            transformador.transform(new DOMSource(documento), new StreamResult(destino.toFile()));
        } catch (ParserConfigurationException | TransformerException ex) {
            throw new IOException("No se pudo exportar el XML: " + ex.getMessage(), ex);
        }
    }

    // ---------- IMPORTAR XML DE FORMA SEGURA (Relación 3 - Ej. 4) ----------
    // Regla: leer y validar TODO en una lista temporal; solo si no hay errores
    // Main sustituye la lista real. Un XML erróneo NO destruye lo que ya había.
    static List<Equipo> importarXml(Path ruta) throws IOException {
        if (Files.notExists(ruta)) {
            throw new IOException("No existe el fichero " + ruta);
        }
        try {
            DocumentBuilderFactory fabrica = DocumentBuilderFactory.newInstance();
            // Seguridad: sin DTD ni entidades externas (ANTES de parse)
            fabrica.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
            fabrica.setFeature("http://xml.org/sax/features/external-general-entities", false);
            fabrica.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
            fabrica.setXIncludeAware(false);
            fabrica.setExpandEntityReferences(false);

            Document documento = fabrica.newDocumentBuilder().parse(ruta.toFile());
            NodeList elementos = documento.getElementsByTagName("equipo");

            List<Equipo> importados = new ArrayList<>();        // lista TEMPORAL
            for (int i = 0; i < elementos.getLength(); i++) {
                Element xml = (Element) elementos.item(i);
                NodeList nombres = xml.getElementsByTagName("nombre");
                NodeList unidades = xml.getElementsByTagName("unidades");
                if (nombres.getLength() != 1 || unidades.getLength() != 1) {
                    throw new IllegalArgumentException("Faltan campos en el equipo " + (i + 1));
                }
                int id = Integer.parseInt(xml.getAttribute("id").trim());
                String nombre = nombres.item(0).getTextContent().trim();
                int uds = Integer.parseInt(unidades.item(0).getTextContent().trim());
                if (id <= 0 || nombre.isEmpty() || uds < 0) {
                    throw new IllegalArgumentException("Datos inválidos en el equipo " + (i + 1));
                }
                if (buscarPorId(importados, id) != null) {
                    throw new IllegalArgumentException("ID duplicado: " + id);
                }
                importados.add(new Equipo(id, nombre, uds));
            }
            return importados;                                  // solo si TODO fue bien
        } catch (Exception ex) {
            throw new IOException("No se pudo importar el XML: " + ex.getMessage(), ex);
        }
    }
}

/*
======================================================================
[BUSCAR: JSON] - JACKSON (RELACIÓN 3 - EJ. 5) - COMENTADO PARA QUE COMPILE
======================================================================
Necesita proyecto Maven. Descomenta este bloque en un proyecto con Jackson.

1) pom.xml (dentro de <dependencies>):
   <dependency>
     <groupId>com.fasterxml.jackson.core</groupId>
     <artifactId>jackson-databind</artifactId>
     <version>2.18.3</version>
   </dependency>
   y Java 17 en las propiedades (maven.compiler.source / target = 17).

2) Código:

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

class EquiposJson {
    // record: clase de solo datos; genera id(), nombre(), unidades()
    public record EquipoJson(int id, String nombre, int unidades) {}

    private static final ObjectMapper MAPPER = new ObjectMapper();

    // EXPORTAR (JSON con saltos de línea e indentación)
    static void exportar(List<EquipoJson> equipos, Path ruta) throws IOException {
        Files.createDirectories(ruta.getParent());
        MAPPER.writerWithDefaultPrettyPrinter().writeValue(ruta.toFile(), equipos);
    }

    // IMPORTAR + VALIDAR: si el JSON está mal formado, readValue lanza una
    // excepción (subclase de IOException). Quien llama la captura, muestra
    // el error y CONSERVA los datos anteriores.
    static List<EquipoJson> importar(Path ruta) throws IOException {
        if (Files.notExists(ruta)) {
            throw new IOException("No existe el fichero " + ruta);
        }
        List<EquipoJson> leidos = MAPPER.readValue(ruta.toFile(),
                new TypeReference<List<EquipoJson>>() {});      // lista, no un solo objeto
        List<Integer> ids = new ArrayList<>();
        for (EquipoJson e : leidos) {
            if (e.id() <= 0 || e.nombre() == null || e.nombre().isBlank() || e.unidades() < 0) {
                throw new IOException("Datos inválidos: " + e);
            }
            if (ids.contains(e.id())) {
                throw new IOException("ID duplicado: " + e.id());
            }
            ids.add(e.id());
        }
        return leidos;                                          // solo si todo es válido
    }
}
======================================================================
*/

// ====================================================================
// [BUSCAR: REPOSITORIO] - RELACIÓN 3, EJ. 6 y 7 (interfaz intercambiable)
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- Main trabaja SOLO contra la interfaz. En Main NO debe aparecer Files, Path,
  BufferedReader ni BufferedWriter.
- Cambiar de TXT a binario = cambiar UNA línea de Main:
      RepositorioClubes repo = new RepositorioTexto(Path.of("datos", "clubes.txt"));
      RepositorioClubes repo = new RepositorioBinario(Path.of("datos", "clubes.dat"));
- Si el fichero no existe, cargarTodos() devuelve lista vacía (no falla).
*/
class Club implements Serializable {
    private static final long serialVersionUID = 1L;

    private final int id;
    private final String nombre;
    private String ciudad;

    Club(int id, String nombre, String ciudad) {
        this.id = id;
        this.nombre = nombre;
        this.ciudad = ciudad;
    }

    int getId() { return id; }
    String getNombre() { return nombre; }
    String getCiudad() { return ciudad; }
    void setCiudad(String ciudad) { this.ciudad = ciudad; }

    @Override
    public String toString() {
        return id + " | " + nombre + " | " + ciudad;
    }
}

interface RepositorioClubes {
    void guardarTodos(List<Club> clubes) throws IOException;
    List<Club> cargarTodos() throws IOException;
}

class RepositorioTexto implements RepositorioClubes {
    private final Path ruta;

    RepositorioTexto(Path ruta) {
        this.ruta = ruta;
    }

    @Override
    public void guardarTodos(List<Club> clubes) throws IOException {
        if (ruta.getParent() != null) {
            Files.createDirectories(ruta.getParent());
        }
        List<String> lineas = new ArrayList<>();
        for (Club club : clubes) {
            lineas.add(club.getId() + ";" + club.getNombre() + ";" + club.getCiudad());
        }
        Files.write(ruta, lineas, StandardCharsets.UTF_8);
    }

    @Override
    public List<Club> cargarTodos() throws IOException {
        List<Club> clubes = new ArrayList<>();
        if (Files.notExists(ruta)) {
            return clubes;                                      // sin fichero -> lista vacía
        }
        List<String> lineas = Files.readAllLines(ruta, StandardCharsets.UTF_8);
        for (int i = 0; i < lineas.size(); i++) {
            if (lineas.get(i).isBlank()) {
                continue;
            }
            String[] c = lineas.get(i).split(";", -1);
            if (c.length != 3) {
                throw new IOException("Línea " + (i + 1) + ": se esperaban 3 campos");
            }
            try {
                int id = Integer.parseInt(c[0].trim());
                clubes.add(new Club(id, c[1].trim(), c[2].trim()));
            } catch (NumberFormatException e) {
                throw new IOException("Línea " + (i + 1) + ": ID no numérico", e);
            }
        }
        return clubes;
    }
}

class RepositorioBinario implements RepositorioClubes {
    private final Path ruta;

    RepositorioBinario(Path ruta) {
        this.ruta = ruta;
    }

    @Override
    public void guardarTodos(List<Club> clubes) throws IOException {
        if (ruta.getParent() != null) {
            Files.createDirectories(ruta.getParent());
        }
        try (ObjectOutputStream salida = new ObjectOutputStream(Files.newOutputStream(ruta))) {
            salida.writeObject(new ArrayList<>(clubes));
        }
    }

    @Override
    public List<Club> cargarTodos() throws IOException {
        List<Club> clubes = new ArrayList<>();
        if (Files.notExists(ruta)) {
            return clubes;
        }
        try (ObjectInputStream entrada = new ObjectInputStream(Files.newInputStream(ruta))) {
            Object dato = entrada.readObject();
            if (!(dato instanceof List<?> lista)) {
                throw new IOException("El archivo no contiene una lista");
            }
            for (Object elemento : lista) {
                if (!(elemento instanceof Club club)) {
                    throw new IOException("Hay un elemento que no es un Club");
                }
                clubes.add(club);
            }
        } catch (ClassNotFoundException ex) {
            throw new IOException("Clase no encontrada al leer el binario", ex);
        }
        return clubes;
    }
}

// Ejemplo de Main que solo conoce la interfaz (no usa Files ni Path directamente)
class MainRepositorio {
    public static void main(String[] args) {
        // >>> ÚNICA LÍNEA QUE CAMBIA entre TXT y binario <<<
        RepositorioClubes repo = new RepositorioTexto(Path.of("datos", "clubes.txt"));
        try {
            List<Club> clubes = repo.cargarTodos();
            clubes.add(new Club(clubes.size() + 1, "Nuevo Club", "Ciudad"));
            repo.guardarTodos(clubes);
            for (Club club : clubes) {
                System.out.println(club);
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}

// ====================================================================
// [BUSCAR: MAIN CSV] - MENÚ COMPLETO DEL EJERCICIO 1 (TODO 1.6)
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- En el examen esta clase se llama Main.
- Patrón de cada opción: pedir datos -> comprobar null (no es número) ->
  llamar al gestor -> mostrar mensaje según el boolean que devuelve.
- Después de restaurar hay que RECARGAR la lista: lista = cargar().
- Todo el switch va dentro de un try/catch(IOException): errores de datos
  o de disco se muestran con e.getMessage() y el menú sigue funcionando.
*/
class MainInscripciones {

    static void mostrarMenu() {
        System.out.println();
        System.out.println("=== GESTOR DE INSCRIPCIONES ===");
        System.out.println("1. Listar inscripciones");
        System.out.println("2. Buscar por ID");
        System.out.println("3. Añadir inscripción");
        System.out.println("4. Modificar plazas");
        System.out.println("5. Eliminar inscripción");
        System.out.println("6. Restaurar copia");
        System.out.println("0. Salir");
    }

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        List<Inscripcion> lista;
        try {
            lista = GestorInscripciones.cargar();
        } catch (IOException e) {
            System.out.println("No se pudo cargar el CSV: " + e.getMessage());
            return;
        }

        int opcion;
        do {
            mostrarMenu();
            Integer leida = Funciones.leerEntero(teclado, "Opción: ");
            opcion = (leida == null) ? -1 : leida;       // texto no numérico -> opción inválida

            try {
                switch (opcion) {
                    case 1 -> {
                        if (lista.isEmpty()) {
                            System.out.println("No hay inscripciones.");
                        }
                        for (Inscripcion inscripcion : lista) {
                            System.out.println(inscripcion);
                        }
                    }
                    case 2 -> {
                        Integer id = Funciones.leerEntero(teclado, "ID a buscar: ");
                        if (id == null) {
                            System.out.println("El ID debe ser un número.");
                        } else {
                            Inscripcion encontrada = GestorInscripciones.buscarPorId(lista, id);
                            if (encontrada == null) {
                                System.out.println("No existe la inscripción " + id);
                            } else {
                                System.out.println(encontrada);
                            }
                        }
                    }
                    case 3 -> {
                        Integer id = Funciones.leerEntero(teclado, "ID: ");
                        String persona = Funciones.leerTexto(teclado, "Persona: ");
                        String taller = Funciones.leerTexto(teclado, "Taller: ");
                        Integer plazas = Funciones.leerEntero(teclado, "Plazas: ");
                        if (id == null || plazas == null || id <= 0 || plazas < 0
                                || persona.isEmpty() || taller.isEmpty()) {
                            System.out.println("Datos no válidos. No se ha añadido nada.");
                        } else if (GestorInscripciones.anadir(lista,
                                new Inscripcion(id, persona, taller, plazas))) {
                            System.out.println("Inscripción añadida.");
                        } else {
                            System.out.println("Ya existe una inscripción con ese ID.");
                        }
                    }
                    case 4 -> {                                  // TODO 1.6: modificar plazas
                        Integer id = Funciones.leerEntero(teclado, "ID: ");
                        Integer plazas = Funciones.leerEntero(teclado, "Nuevas plazas: ");
                        if (id == null || plazas == null) {
                            System.out.println("Debes escribir números.");
                        } else if (GestorInscripciones.modificarPlazas(lista, id, plazas)) {
                            System.out.println("Plazas modificadas correctamente.");
                        } else {
                            System.out.println("No se modificó nada: ID inexistente o plazas negativas.");
                        }
                    }
                    case 5 -> {                                  // TODO 1.6: eliminar
                        Integer id = Funciones.leerEntero(teclado, "ID a eliminar: ");
                        if (id == null) {
                            System.out.println("El ID debe ser un número.");
                        } else if (GestorInscripciones.eliminar(lista, id)) {
                            System.out.println("Inscripción eliminada.");
                        } else {
                            System.out.println("No existe la inscripción " + id);
                        }
                    }
                    case 6 -> {                                  // TODO 1.6: restaurar con S/N
                        if (!GestorInscripciones.hayCopia()) {
                            System.out.println("No hay copia de seguridad que restaurar.");
                        } else if (Funciones.confirmar(teclado,
                                "Se sustituirán los datos actuales por la copia. ¿Continuar?")) {
                            if (GestorInscripciones.restaurar()) {
                                lista = GestorInscripciones.cargar();   // RECARGAR tras restaurar
                                System.out.println("Copia restaurada.");
                            }
                        } else {
                            System.out.println("Restauración cancelada.");
                        }
                    }
                    case 0 -> System.out.println("Hasta luego.");
                    default -> System.out.println("Opción no válida.");
                }
            } catch (IOException e) {
                System.out.println("Error de entrada/salida: " + e.getMessage());
            }
        } while (opcion != 0);
    }
}

// ====================================================================
// [BUSCAR: MAIN BINARIO] - MENÚ COMPLETO DEL EJERCICIO 2 (TODO 2.5)
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- Opción 3 cambia SOLO en memoria. Para persistir hay que elegir "Guardar" (4).
- Opción 5 recarga desde disco: sirve para comprobar que lo no guardado se pierde
  (cambiar a 12, recargar sin guardar -> vuelven las 5 unidades originales).
- Opción 6 exporta el XML con la lista que hay ahora en memoria.
*/
class MainEquipos {

    static void mostrarMenu() {
        System.out.println();
        System.out.println("=== ARCHIVO DE EQUIPOS ===");
        System.out.println("1. Listar equipos");
        System.out.println("2. Buscar por ID");
        System.out.println("3. Cambiar unidades (solo en memoria)");
        System.out.println("4. Guardar en disco");
        System.out.println("5. Recargar desde disco (descarta lo no guardado)");
        System.out.println("6. Exportar a XML");
        System.out.println("0. Salir");
    }

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        List<Equipo> equipos;
        try {
            equipos = RepositorioEquipos.cargar();
        } catch (IOException e) {
            System.out.println("No se pudo cargar el archivo: " + e.getMessage());
            return;
        }

        int opcion;
        do {
            mostrarMenu();
            Integer leida = Funciones.leerEntero(teclado, "Opción: ");
            opcion = (leida == null) ? -1 : leida;

            try {
                switch (opcion) {
                    case 1 -> {
                        if (equipos.isEmpty()) {
                            System.out.println("No hay equipos.");
                        }
                        for (Equipo equipo : equipos) {
                            System.out.println(equipo);
                        }
                    }
                    case 2 -> {
                        Integer id = Funciones.leerEntero(teclado, "ID a buscar: ");
                        if (id == null) {
                            System.out.println("El ID debe ser un número.");
                        } else {
                            Equipo encontrado = RepositorioEquipos.buscarPorId(equipos, id);
                            System.out.println(encontrado == null
                                    ? "No existe el equipo " + id : encontrado.toString());
                        }
                    }
                    case 3 -> {                                  // TODO 2.5: modificar
                        Integer id = Funciones.leerEntero(teclado, "ID: ");
                        Integer unidades = Funciones.leerEntero(teclado, "Nuevas unidades: ");
                        if (id == null || unidades == null) {
                            System.out.println("Debes escribir números.");
                        } else if (RepositorioEquipos.cambiarUnidades(equipos, id, unidades)) {
                            System.out.println("Cambiado en memoria. Recuerda guardar (opción 4).");
                        } else {
                            System.out.println("ID inexistente o unidades no válidas.");
                        }
                    }
                    case 4 -> {                                  // guardado explícito
                        RepositorioEquipos.guardar(equipos);
                        System.out.println("Guardado en disco.");
                    }
                    case 5 -> {                                  // TODO 2.5: recargar
                        equipos = RepositorioEquipos.cargar();
                        System.out.println("Recargado desde disco: " + equipos.size() + " equipos.");
                    }
                    case 6 -> {                                  // TODO 2.5: exportar XML
                        RepositorioEquipos.exportarXml(equipos);
                        System.out.println("XML exportado en " + RepositorioEquipos.XML);
                    }
                    case 0 -> System.out.println("Hasta luego.");
                    default -> System.out.println("Opción no válida.");
                }
            } catch (IOException e) {
                System.out.println("Error: " + e.getMessage());
            }
        } while (opcion != 0);
    }
}

// ====================================================================
// [BUSCAR: GESTOR DIRECTO] - VARIANTE: CADA MÉTODO LEE Y ESCRIBE EL FICHERO
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- Algunos enunciados NO pasan la lista en memoria: cada operación carga el
  CSV, cambia lo que toca y vuelve a guardar. Es el estilo de este bloque.
- Usa cargarCsv(), buscarPorId(), guardar() y crearCopia() de GestorInscripciones.
- Patrón: cargar -> buscar -> (si no existe: false) -> copia -> cambiar -> guardar.
*/
class GestorInscripcionesDirecto {

    // Modificar plazas leyendo y escribiendo el fichero
    static boolean modificarPlazas(int id, int nuevasPlazas) throws IOException {
        if (nuevasPlazas < 0) {
            return false;
        }
        List<Inscripcion> lista = GestorInscripciones.cargar();
        Inscripcion inscripcion = GestorInscripciones.buscarPorId(lista, id);
        if (inscripcion == null) {
            return false;                                 // no existe: NO se toca el fichero
        }
        GestorInscripciones.crearCopia();                 // copia ANTES de reescribir
        inscripcion.setPlazas(nuevasPlazas);
        GestorInscripciones.guardar(lista);
        return true;
    }

    // Eliminar leyendo y escribiendo el fichero
    static boolean eliminar(int id) throws IOException {
        List<Inscripcion> lista = GestorInscripciones.cargar();
        List<Inscripcion> limpia = new ArrayList<>();
        boolean encontrado = false;
        for (Inscripcion inscripcion : lista) {
            if (inscripcion.getId() == id) {
                encontrado = true;                        // este NO pasa a la lista limpia
            } else {
                limpia.add(inscripcion);
            }
        }
        if (!encontrado) {
            return false;
        }
        GestorInscripciones.crearCopia();                 // copia ANTES de borrar (para poder restaurar)
        GestorInscripciones.guardar(limpia);
        return true;
    }
}

// ====================================================================
// [BUSCAR: PRODUCTO] - MODELO (id;nombre;precio;stock) CON DECIMAL
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- El precio es double: en el CSV va con PUNTO (24.95).
- Serializable + serialVersionUID para poder guardarlo en binario.
- Si en el examen el modelo ya viene hecho, mira SOLO qué getters tiene.
*/
class Producto implements Serializable {
    private static final long serialVersionUID = 1L;

    private final int id;
    private final String nombre;
    private double precio;
    private int stock;

    Producto(int id, String nombre, double precio, int stock) {
        this.id = id;
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }

    int getId() { return id; }
    String getNombre() { return nombre; }
    double getPrecio() { return precio; }
    int getStock() { return stock; }
    void setPrecio(double precio) { this.precio = precio; }
    void setStock(int stock) { this.stock = stock; }

    String toCsv() {
        return id + ";" + nombre + ";" + precio + ";" + stock;
    }

    @Override
    public String toString() {
        return String.format("%d | %s | %.2f € | stock: %d", id, nombre, precio, stock);
    }
}

// ====================================================================
// [BUSCAR: INVENTARIO] - LISTA EN MEMORIA: BUSCAR POR ID · ALTA · MODIFICAR
//                        · ELIMINAR · INFORMES
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- Esta clase trabaja SOLO EN MEMORIA: NO usa ficheros, ni System.out, ni
  Scanner. Guardar en fichero lo hace otra clase (RepositorioCsvProductos...).
- Validaciones de alta: lanzan IllegalArgumentException con un mensaje.
- modificar / eliminar: devuelven boolean (false = no existe o dato inválido).
- [BUSCAR: INFORMES] está abajo: total, más caro, stock bajo, media, filtros...
*/
class Inventario {
    private final List<Producto> productos = new ArrayList<>();

    public List<Producto> getProductos() { return productos; }
    public boolean estaVacio() { return productos.isEmpty(); }

    // Sustituye todo el contenido (datos ya validados al cargar/importar)
    public void reemplazarTodo(List<Producto> nuevos) {
        productos.clear();
        productos.addAll(nuevos);
    }

    // ------------------- BUSCAR POR ID (devuelve el objeto o null) -------------------
    public Producto buscarPorId(int id) {
        for (Producto p : productos) {
            if (p.getId() == id) {
                return p;
            }
        }
        return null;
    }

    // Buscar por nombre EXACTO ignorando mayúsculas y espacios extremos
    public Producto buscarPorNombre(String nombre) {
        for (Producto p : productos) {
            if (p.getNombre().trim().equalsIgnoreCase(nombre.trim())) {
                return p;
            }
        }
        return null;
    }

    // Buscar varios: el nombre CONTIENE el texto (ignorando mayúsculas)
    public List<Producto> buscarPorTexto(String texto) {
        List<Producto> encontrados = new ArrayList<>();
        String buscado = texto.trim().toLowerCase();
        for (Producto p : productos) {
            if (p.getNombre().toLowerCase().contains(buscado)) {
                encontrados.add(p);
            }
        }
        return encontrados;
    }

    // ------------------- ALTA (rechaza con IllegalArgumentException) -------------------
    public void anadir(Producto nuevo) {
        if (nuevo.getId() <= 0) {
            throw new IllegalArgumentException("El ID debe ser mayor que 0.");
        }
        if (buscarPorId(nuevo.getId()) != null) {
            throw new IllegalArgumentException("Ya existe un producto con el ID " + nuevo.getId() + ".");
        }
        String nombre = nuevo.getNombre().trim();
        if (nombre.isEmpty()) {
            throw new IllegalArgumentException("El nombre no puede estar vacío.");
        }
        for (Producto p : productos) {                       // nombre repetido (sin mayúsculas/espacios)
            if (p.getNombre().trim().equalsIgnoreCase(nombre)) {
                throw new IllegalArgumentException("Ya existe un producto con el nombre \"" + nombre + "\".");
            }
        }
        if (nuevo.getPrecio() < 0) {
            throw new IllegalArgumentException("El precio no puede ser negativo.");
        }
        if (nuevo.getStock() < 0) {
            throw new IllegalArgumentException("El stock no puede ser negativo.");
        }
        productos.add(nuevo);
    }

    // ------------------- MODIFICAR (boolean: false = no existe o dato inválido) -------------------
    public boolean modificarStock(int id, int nuevoStock) {
        if (nuevoStock < 0) {
            return false;
        }
        Producto producto = buscarPorId(id);
        if (producto == null) {
            return false;
        }
        producto.setStock(nuevoStock);
        return true;
    }

    public boolean modificarPrecio(int id, double nuevoPrecio) {
        if (nuevoPrecio < 0) {
            return false;
        }
        Producto producto = buscarPorId(id);
        if (producto == null) {
            return false;
        }
        producto.setPrecio(nuevoPrecio);
        return true;
    }

    // ------------------- ELIMINAR (true si existía y se quitó) -------------------
    public boolean eliminar(int id) {
        Producto producto = buscarPorId(id);
        if (producto == null) {
            return false;
        }
        productos.remove(producto);
        return true;
    }

    // ====================================================================
    // [BUSCAR: INFORMES] - 3 PATRONES: ACUMULADOR · EL MEJOR · FILTRO
    // ====================================================================
    // Patrón ACUMULADOR: empieza en 0 y va sumando
    public double valorTotal() {
        double total = 0;
        for (Producto p : productos) {
            total += p.getPrecio() * p.getStock();
        }
        return total;
    }

    public int stockTotal() {
        int total = 0;
        for (Producto p : productos) {
            total += p.getStock();
        }
        return total;
    }

    // Media: suma / cantidad (cuidado con dividir por 0)
    public double precioMedio() {
        if (productos.isEmpty()) {
            return 0;
        }
        double suma = 0;
        for (Producto p : productos) {
            suma += p.getPrecio();
        }
        return suma / productos.size();
    }

    // Patrón EL MEJOR HASTA AHORA: null si la lista está vacía
    public Producto masCaro() {
        Producto mejor = null;
        for (Producto p : productos) {
            if (mejor == null || p.getPrecio() > mejor.getPrecio()) {
                mejor = p;
            }
        }
        return mejor;
    }

    public Producto masBarato() {
        Producto mejor = null;
        for (Producto p : productos) {
            if (mejor == null || p.getPrecio() < mejor.getPrecio()) {
                mejor = p;
            }
        }
        return mejor;
    }

    // Patrón FILTRO: lista nueva con los que cumplen la condición
    public List<Producto> stockBajo(int umbral) {              // stock ESTRICTAMENTE menor
        List<Producto> bajos = new ArrayList<>();
        for (Producto p : productos) {
            if (p.getStock() < umbral) {
                bajos.add(p);
            }
        }
        return bajos;
    }

    public List<Producto> entrePrecios(double minimo, double maximo) {
        List<Producto> resultado = new ArrayList<>();
        for (Producto p : productos) {
            if (p.getPrecio() >= minimo && p.getPrecio() <= maximo) {
                resultado.add(p);
            }
        }
        return resultado;
    }

    // Patrón CONTADOR
    public int contarSinStock() {
        int cuantos = 0;
        for (Producto p : productos) {
            if (p.getStock() == 0) {
                cuantos++;
            }
        }
        return cuantos;
    }

    // ORDENAR (copia ordenada; no cambia la lista original). Fuera del temario, por si acaso.
    public List<Producto> ordenadosPorPrecio() {
        List<Producto> copia = new ArrayList<>(productos);
        copia.sort(Comparator.comparingDouble(Producto::getPrecio));
        return copia;
    }

    public List<Producto> ordenadosPorNombre() {
        List<Producto> copia = new ArrayList<>(productos);
        copia.sort(Comparator.comparing(Producto::getNombre, String.CASE_INSENSITIVE_ORDER));
        return copia;
    }
}

// ====================================================================
// [BUSCAR: CARGAR CSV PRODUCTOS] [BUSCAR: GUARDAR CSV PRODUCTOS]
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- cargar(): omite la cabecera, valida cada fila y lanza IOException con el
  número de línea (la cabecera es la línea 1). Devuelve la lista SOLO si
  todo es correcto.
- guardar(): escribe la CABECERA y después todos los registros.
- Si el enunciado dice "si no existe, lista vacía", cambia el throw por
  return lista;  (en la línea marcada).
*/
class RepositorioCsvProductos {
    static final Path RUTA = Path.of("datos", "inventario.csv");          // <<< ADAPTAR
    static final String CABECERA = "id;nombre;precio;stock";               // <<< ADAPTAR

    static boolean existe() {
        return Files.exists(RUTA);
    }

    // ---------------- CARGAR ----------------
    static List<Producto> cargar() throws IOException {
        List<Producto> lista = new ArrayList<>();
        if (Files.notExists(RUTA)) {
            throw new IOException("No existe el archivo " + RUTA);         // o: return lista;
        }
        List<String> lineas = Files.readAllLines(RUTA, StandardCharsets.UTF_8);
        for (int i = 1; i < lineas.size(); i++) {                          // i = 1 -> salta la cabecera
            String linea = lineas.get(i);
            if (linea.isBlank()) {
                continue;
            }
            int numLinea = i + 1;
            String[] campos = linea.split(";", -1);
            if (campos.length != 4) {                                      // <<< ADAPTAR (nº de campos)
                throw new IOException("Línea " + numLinea + ": se esperaban 4 campos");
            }
            int id;
            double precio;
            int stock;
            try {                                                          // <<< ADAPTAR (índices y tipos)
                id = Integer.parseInt(campos[0].trim());
                precio = Double.parseDouble(campos[2].trim());
                stock = Integer.parseInt(campos[3].trim());
            } catch (NumberFormatException e) {
                throw new IOException("Línea " + numLinea + ": ID, precio o stock no son números válidos", e);
            }
            String nombre = campos[1].trim();
            if (id <= 0 || nombre.isEmpty() || precio < 0 || stock < 0) {
                throw new IOException("Línea " + numLinea + ": datos no válidos");
            }
            for (Producto p : lista) {                                     // ID repetido (sin buscarPorId)
                if (p.getId() == id) {
                    throw new IOException("Línea " + numLinea + ": ID repetido (" + id + ")");
                }
            }
            lista.add(new Producto(id, nombre, precio, stock));            // <<< ADAPTAR (clase)
        }
        return lista;
    }

    // ---------------- GUARDAR ----------------
    static void guardar(List<Producto> productos) throws IOException {
        Files.createDirectories(RUTA.getParent());
        List<String> lineas = new ArrayList<>();
        lineas.add(CABECERA);                                              // sin cabecera se pierde el 1.er registro al cargar
        for (Producto p : productos) {
            lineas.add(p.toCsv());
        }
        Files.write(RUTA, lineas, StandardCharsets.UTF_8);
    }
}

// ====================================================================
// [BUSCAR: COPIAS] - COPIA DE SEGURIDAD Y RESTAURAR (simple, con fecha, la más reciente)
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- crearCopia(): false si no hay fichero que copiar.
- restaurar(): false (sin tocar nada) si no hay copia. La CONFIRMACIÓN S/N
  se pide en Main; después de restaurar, Main debe RECARGAR los datos.
- Copia con fecha: varias copias (nombre + yyyyMMdd_HHmmss).
- "Restaurar la más reciente": el nombre mayor (compareTo) es la más nueva.
*/
class GestorCopias {
    static final Path ORIGEN = RepositorioCsvProductos.RUTA;                 // <<< ADAPTAR
    static final Path COPIA = Path.of("datos", "copias", "inventario.bak");  // <<< ADAPTAR

    static boolean hayCopia() {
        return Files.exists(COPIA);
    }

    static boolean crearCopia() throws IOException {
        if (Files.notExists(ORIGEN)) {
            return false;
        }
        Files.createDirectories(COPIA.getParent());
        Files.copy(ORIGEN, COPIA, StandardCopyOption.REPLACE_EXISTING);
        return true;
    }

    static boolean restaurar() throws IOException {
        if (Files.notExists(COPIA)) {
            return false;
        }
        Files.copy(COPIA, ORIGEN, StandardCopyOption.REPLACE_EXISTING);
        return true;
    }

    // ---- Copias con fecha: datos/copias/inventario.csv_20261102_221500.bak ----
    static Path crearCopiaConFecha() throws IOException {
        if (Files.notExists(ORIGEN)) {
            return null;
        }
        return Funciones.crearCopiaConFecha(ORIGEN, COPIA.getParent());
    }

    // La copia más reciente: el nombre que empiece por el prefijo y sea MAYOR
    static Path buscarCopiaMasReciente(Path carpetaCopias, String prefijo) throws IOException {
        if (Files.notExists(carpetaCopias)) {
            return null;
        }
        Path mejor = null;
        try (DirectoryStream<Path> elementos = Files.newDirectoryStream(carpetaCopias)) {
            for (Path elemento : elementos) {
                if (!Files.isRegularFile(elemento)) {
                    continue;
                }
                String nombre = elemento.getFileName().toString();
                if (!nombre.startsWith(prefijo)) {
                    continue;
                }
                if (mejor == null || nombre.compareTo(mejor.getFileName().toString()) > 0) {
                    mejor = elemento;
                }
            }
        }
        return mejor;                                                        // null si no hay ninguna
    }

    static boolean restaurarMasReciente() throws IOException {
        Path reciente = buscarCopiaMasReciente(COPIA.getParent(), ORIGEN.getFileName() + "_");
        if (reciente == null) {
            return false;
        }
        Files.copy(reciente, ORIGEN, StandardCopyOption.REPLACE_EXISTING);
        return true;
    }
}

// ====================================================================
// [BUSCAR: BINARIO PRODUCTOS] - GUARDAR/CARGAR LA LISTA CON Serializable
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- Es IGUAL que RepositorioEquipos: solo cambia la clase (Producto) y la ruta.
- Guardar: lista COMPLETA con UN writeObject, sin APPEND.
- Cargar: readObject() como Object -> instanceof List<?> -> instanceof de
  cada elemento -> IDs repetidos. ClassNotFoundException -> IOException.
- Sin fichero: lista vacía (comprueba existe() en Main antes de sustituir
  datos, para no vaciar el inventario por error).
*/
class RepositorioBinarioProductos {
    static final Path RUTA = Path.of("datos", "inventario.dat");             // <<< ADAPTAR

    static boolean existe() {
        return Files.exists(RUTA);
    }

    static void guardar(List<Producto> productos) throws IOException {
        Files.createDirectories(RUTA.getParent());
        try (ObjectOutputStream salida = new ObjectOutputStream(Files.newOutputStream(RUTA))) {
            salida.writeObject(new ArrayList<>(productos));
        }
    }

    static List<Producto> cargar() throws IOException {
        List<Producto> lista = new ArrayList<>();
        if (Files.notExists(RUTA)) {
            return lista;
        }
        try (ObjectInputStream entrada = new ObjectInputStream(Files.newInputStream(RUTA))) {
            Object dato = entrada.readObject();
            if (!(dato instanceof List<?> datos)) {
                throw new IOException("El archivo no contiene una lista");
            }
            for (Object elemento : datos) {
                if (!(elemento instanceof Producto producto)) {                // <<< ADAPTAR (clase)
                    throw new IOException("La lista contiene un elemento que no es un Producto");
                }
                for (Producto p : lista) {
                    if (p.getId() == producto.getId()) {
                        throw new IOException("ID repetido en el archivo: " + producto.getId());
                    }
                }
                lista.add(producto);
            }
        } catch (ClassNotFoundException e) {
            throw new IOException("No se encuentra la clase de los objetos guardados", e);
        }
        return lista;
    }
}

// ====================================================================
// [BUSCAR: XML PRODUCTOS] - EXPORTAR · IMPORTAR SEGURO · FUSIONAR
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN:
- exportar: DOM (createElement, setAttribute, setTextContent, appendChild)
  + Transformer con UTF-8 e INDENT. NO concatenes Strings: el & rompe el XML.
- importar: sin DTD ni entidades externas ANTES de parse(); valida TODO en
  una lista temporal; devuelve la lista solo si no hay errores.
- fusionar: añade solo los importados cuyo ID no exista y devuelve cuántos.
- Formato: <inventario><producto id="1"><nombre/><precio/><stock/></producto></inventario>
*/
class GestorXmlProductos {
    static final Path EXPORTACION = Path.of("datos", "inventario.xml");      // <<< ADAPTAR

    static void exportar(List<Producto> productos, Path destino) throws IOException {
        try {
            Document documento = DocumentBuilderFactory.newInstance().newDocumentBuilder().newDocument();
            Element raiz = documento.createElement("inventario");            // <<< ADAPTAR (raíz)
            documento.appendChild(raiz);

            for (Producto p : productos) {
                Element elemento = documento.createElement("producto");      // <<< ADAPTAR (elemento)
                elemento.setAttribute("id", String.valueOf(p.getId()));

                Element nombre = documento.createElement("nombre");
                nombre.setTextContent(p.getNombre());
                Element precio = documento.createElement("precio");
                precio.setTextContent(String.valueOf(p.getPrecio()));
                Element stock = documento.createElement("stock");
                stock.setTextContent(String.valueOf(p.getStock()));

                elemento.appendChild(nombre);
                elemento.appendChild(precio);
                elemento.appendChild(stock);
                raiz.appendChild(elemento);
            }

            if (destino.getParent() != null) {
                Files.createDirectories(destino.getParent());
            }
            Transformer transformador = TransformerFactory.newInstance().newTransformer();
            transformador.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
            transformador.setOutputProperty(OutputKeys.INDENT, "yes");
            transformador.transform(new DOMSource(documento), new StreamResult(destino.toFile()));
        } catch (ParserConfigurationException | TransformerException e) {
            throw new IOException("No se pudo exportar el XML: " + e.getMessage(), e);
        }
    }

    static List<Producto> importar(Path ruta) throws IOException {
        if (Files.notExists(ruta)) {
            throw new IOException("No existe el archivo " + ruta);
        }
        try {
            DocumentBuilderFactory fabrica = DocumentBuilderFactory.newInstance();
            fabrica.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
            fabrica.setFeature("http://xml.org/sax/features/external-general-entities", false);
            fabrica.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
            fabrica.setXIncludeAware(false);
            fabrica.setExpandEntityReferences(false);

            Document documento = fabrica.newDocumentBuilder().parse(ruta.toFile());
            NodeList elementos = documento.getElementsByTagName("producto");   // <<< ADAPTAR

            List<Producto> importados = new ArrayList<>();                     // lista TEMPORAL
            for (int i = 0; i < elementos.getLength(); i++) {
                Element xml = (Element) elementos.item(i);
                int numero = i + 1;
                NodeList nombres = xml.getElementsByTagName("nombre");
                NodeList precios = xml.getElementsByTagName("precio");
                NodeList stocks = xml.getElementsByTagName("stock");
                if (nombres.getLength() != 1 || precios.getLength() != 1 || stocks.getLength() != 1) {
                    throw new IllegalArgumentException("Faltan campos en el producto " + numero);
                }
                int id;
                double precio;
                int stock;
                try {
                    id = Integer.parseInt(xml.getAttribute("id").trim());
                    precio = Double.parseDouble(precios.item(0).getTextContent().trim());
                    stock = Integer.parseInt(stocks.item(0).getTextContent().trim());
                } catch (NumberFormatException e) {
                    throw new IllegalArgumentException("Producto " + numero + ": número no válido");
                }
                String nombre = nombres.item(0).getTextContent().trim();
                if (id <= 0 || nombre.isEmpty() || precio < 0 || stock < 0) {
                    throw new IllegalArgumentException("Datos no válidos en el producto " + numero);
                }
                for (Producto p : importados) {
                    if (p.getId() == id) {
                        throw new IllegalArgumentException("ID repetido: " + id);
                    }
                }
                importados.add(new Producto(id, nombre, precio, stock));
            }
            if (importados.isEmpty()) {
                throw new IllegalArgumentException("El XML no contiene ningún producto");
            }
            return importados;                                                 // solo si TODO es correcto
        } catch (Exception e) {
            throw new IOException("No se pudo importar el XML: " + e.getMessage(), e);
        }
    }

    // Variante con nombre de archivo dentro de datos (así Main no necesita Path)
    static List<Producto> importar(String nombreArchivo) throws IOException {
        return importar(Path.of("datos", nombreArchivo));
    }

    // Fusionar: añade solo los que no existen (por ID). Devuelve cuántos se añadieron.
    static int fusionar(List<Producto> actuales, List<Producto> importados) {
        int anadidos = 0;
        for (Producto nuevo : importados) {
            boolean existe = false;
            for (Producto p : actuales) {
                if (p.getId() == nuevo.getId()) {
                    existe = true;
                    break;
                }
            }
            if (!existe) {
                actuales.add(nuevo);
                anadidos++;
            }
        }
        return anadidos;
    }
}

// ====================================================================
// [BUSCAR: MENU] - PLANTILLAS DE MENÚ Y SUBMENÚ (EL PROFESOR LOS ADORA)
// ====================================================================
/*
CÓMO USAR EN EL EXAMEN (6 patrones):
 1. MENÚ SIMPLE con String y while   -> MainMenuSimple (abajo, estilo Relación 4).
 2. MENÚ con int y do-while          -> MainInventario.main().
 3. SUBMENÚ: método con su propio do-while y "0. Volver" -> menuProductos().
 4. LEER OPCIÓN SEGURA: Integer null -> -1 (texto no cierra el programa).
 5. PEDIR DATOS: leerEntero/leerDecimal devuelven null si no son números:
        if (id == null || precio == null) { mensaje; return; }
 6. CONFIRMACIÓN S/N antes de borrar / sustituir / restaurar:
        if (Funciones.confirmar(teclado, "¿Seguro?")) { ... } else { "cancelado" }
- Cada opción va en su try/catch: IOException (disco), IllegalArgumentException
  (alta inválida), NumberFormatException (si usas Integer.parseInt en Main).
- Un error NUNCA debe cerrar el menú ni dejar el inventario a medias.
- Tras RESTAURAR, importar o cargar: sustituye con reemplazarTodo(...).
*/

// Patrón 1: menú con String + while (como el de tu Relación 4)
class MainMenuSimple {
    private static final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        String opcion = "";
        while (!opcion.equals("0")) {
            System.out.println("\n===== MENÚ =====");
            System.out.println("1. Listar");
            System.out.println("2. Buscar por ID");
            System.out.println("0. Salir");
            System.out.print("Opción: ");
            opcion = sc.nextLine().trim();
            try {
                switch (opcion) {
                    case "1" -> System.out.println("listar...");
                    case "2" -> buscar();
                    case "0" -> System.out.println("Saliendo...");
                    default -> System.out.println("Opción no válida.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Error: introduce un número válido.");
            }
        }
    }

    private static void buscar() throws NumberFormatException {
        System.out.print("ID: ");
        int id = Integer.parseInt(sc.nextLine().trim());      // si no es número -> NumberFormatException
        System.out.println("Buscando " + id);
    }
}

// Patrones 2-6: menú principal + submenús conectados a TODO lo de arriba
class MainInventario {
    private static final Scanner teclado = new Scanner(System.in);
    private static final Inventario inventario = new Inventario();

    public static void main(String[] args) {
        cargarInicial();
        int opcion;
        do {
            System.out.println("\n===== INVENTARIO =====");
            System.out.println("1. Productos");
            System.out.println("2. Informes");
            System.out.println("3. Archivos (CSV, binario, XML, copias)");
            System.out.println("0. Salir");
            opcion = leerOpcion();
            switch (opcion) {
                case 1 -> menuProductos();
                case 2 -> menuInformes();
                case 3 -> menuArchivos();
                case 0 -> salir();
                default -> System.out.println("Opción no válida.");
            }
        } while (opcion != 0);
    }

    // Opción numérica segura: si no es un número devuelve -1
    static int leerOpcion() {
        Integer numero = Funciones.leerEntero(teclado, "Opción: ");
        return (numero == null) ? -1 : numero;
    }

    // Arranque: carga el CSV si existe; si falla, empieza vacío
    static void cargarInicial() {
        if (!RepositorioCsvProductos.existe()) {
            System.out.println("No hay inventario guardado: se empieza vacío.");
            return;
        }
        try {
            inventario.reemplazarTodo(RepositorioCsvProductos.cargar());
            System.out.println("Inventario cargado: " + inventario.getProductos().size() + " productos.");
        } catch (IOException e) {
            System.out.println("No se pudo cargar el CSV: " + e.getMessage());
        }
    }

    // ---------------- SUBMENÚ PRODUCTOS ----------------
    static void menuProductos() {
        int opcion;
        do {
            System.out.println("\n--- PRODUCTOS ---");
            System.out.println("1. Listar");
            System.out.println("2. Buscar por ID");
            System.out.println("3. Añadir");
            System.out.println("4. Modificar stock");
            System.out.println("5. Eliminar");
            System.out.println("0. Volver");
            opcion = leerOpcion();
            try {
                switch (opcion) {
                    case 1 -> listar();
                    case 2 -> buscar();
                    case 3 -> anadir();
                    case 4 -> modificarStock();
                    case 5 -> eliminar();
                    case 0 -> System.out.println("Volviendo...");
                    default -> System.out.println("Opción no válida.");
                }
            } catch (IllegalArgumentException e) {
                System.out.println("Datos no válidos: " + e.getMessage());
            }
        } while (opcion != 0);
    }

    static void listar() {
        if (inventario.estaVacio()) {
            System.out.println("No hay productos.");
            return;
        }
        for (Producto p : inventario.getProductos()) {
            System.out.println(p);
        }
    }

    static void buscar() {
        Integer id = Funciones.leerEntero(teclado, "ID a buscar: ");
        if (id == null) {
            System.out.println("El ID debe ser un número.");
            return;
        }
        Producto encontrado = inventario.buscarPorId(id);
        System.out.println(encontrado == null ? "No existe el producto " + id + "." : encontrado.toString());
    }

    static void anadir() {
        Integer id = Funciones.leerEntero(teclado, "ID: ");
        String nombre = Funciones.leerTexto(teclado, "Nombre: ");
        Double precio = Funciones.leerDecimal(teclado, "Precio: ");
        Integer stock = Funciones.leerEntero(teclado, "Stock: ");
        if (id == null || precio == null || stock == null) {
            System.out.println("El ID, el precio y el stock deben ser números.");
            return;
        }
        inventario.anadir(new Producto(id, nombre, precio, stock));   // lanza IllegalArgumentException si no vale
        System.out.println("Producto añadido.");
    }

    static void modificarStock() {
        Integer id = Funciones.leerEntero(teclado, "ID del producto: ");
        Integer stock = Funciones.leerEntero(teclado, "Nuevo stock: ");
        if (id == null || stock == null) {
            System.out.println("El ID y el stock deben ser números.");
            return;
        }
        if (inventario.modificarStock(id, stock)) {
            System.out.println("Stock modificado.");
        } else {
            System.out.println("No se modificó nada: el ID no existe o el stock es negativo.");
        }
    }

    static void eliminar() {
        Integer id = Funciones.leerEntero(teclado, "ID a eliminar: ");
        if (id == null) {
            System.out.println("El ID debe ser un número.");
            return;
        }
        Producto producto = inventario.buscarPorId(id);
        if (producto == null) {
            System.out.println("No existe el producto " + id + ".");
            return;
        }
        System.out.println(producto);
        if (Funciones.confirmar(teclado, "¿Eliminar este producto?")) {
            inventario.eliminar(id);
            System.out.println("Producto eliminado.");
        } else {
            System.out.println("Operación cancelada.");
        }
    }

    // ---------------- SUBMENÚ INFORMES ----------------
    static void menuInformes() {
        int opcion;
        do {
            System.out.println("\n--- INFORMES ---");
            System.out.println("1. Valor total del inventario");
            System.out.println("2. Producto más caro");
            System.out.println("3. Productos con stock bajo");
            System.out.println("4. Precio medio");
            System.out.println("0. Volver");
            opcion = leerOpcion();
            switch (opcion) {
                case 1 -> System.out.printf("Valor total del inventario: %.2f €%n", inventario.valorTotal());
                case 2 -> {
                    Producto caro = inventario.masCaro();
                    System.out.println(caro == null ? "No hay productos." : "Más caro: " + caro);
                }
                case 3 -> {
                    Integer umbral = Funciones.leerEntero(teclado, "Umbral de stock: ");
                    if (umbral == null || umbral < 0) {
                        System.out.println("El umbral debe ser un número mayor o igual que 0.");
                    } else {
                        List<Producto> bajos = inventario.stockBajo(umbral);
                        if (bajos.isEmpty()) {
                            System.out.println("Ningún producto tiene stock menor que " + umbral + ".");
                        } else {
                            for (Producto p : bajos) {
                                System.out.println(p);
                            }
                        }
                    }
                }
                case 4 -> System.out.printf("Precio medio: %.2f €%n", inventario.precioMedio());
                case 0 -> System.out.println("Volviendo...");
                default -> System.out.println("Opción no válida.");
            }
        } while (opcion != 0);
    }

    // ---------------- SUBMENÚ ARCHIVOS ----------------
    static void menuArchivos() {
        int opcion;
        do {
            System.out.println("\n--- ARCHIVOS ---");
            System.out.println("1. Guardar en CSV");
            System.out.println("2. Cargar desde CSV");
            System.out.println("3. Guardar en binario");
            System.out.println("4. Cargar desde binario");
            System.out.println("5. Exportar a XML");
            System.out.println("6. Importar desde XML (sustituir)");
            System.out.println("7. Importar desde XML (fusionar)");
            System.out.println("8. Crear copia de seguridad");
            System.out.println("9. Restaurar copia de seguridad");
            System.out.println("0. Volver");
            opcion = leerOpcion();
            try {
                switch (opcion) {
                    case 1 -> {
                        RepositorioCsvProductos.guardar(inventario.getProductos());
                        System.out.println("Guardado en " + RepositorioCsvProductos.RUTA + ".");
                    }
                    case 2 -> {
                        if (!RepositorioCsvProductos.existe()) {
                            System.out.println("No existe el archivo CSV.");
                        } else if (Funciones.confirmar(teclado, "Se sustituirán los datos actuales. ¿Continuar?")) {
                            List<Producto> cargados = RepositorioCsvProductos.cargar();  // si falla, NO se toca el inventario
                            inventario.reemplazarTodo(cargados);
                            System.out.println("Cargados " + cargados.size() + " productos.");
                        } else {
                            System.out.println("Operación cancelada.");
                        }
                    }
                    case 3 -> {
                        RepositorioBinarioProductos.guardar(inventario.getProductos());
                        System.out.println("Guardado en " + RepositorioBinarioProductos.RUTA + ".");
                    }
                    case 4 -> {
                        if (!RepositorioBinarioProductos.existe()) {
                            System.out.println("No existe el archivo binario.");
                        } else if (Funciones.confirmar(teclado, "Se sustituirán los datos actuales. ¿Continuar?")) {
                            List<Producto> cargados = RepositorioBinarioProductos.cargar();
                            inventario.reemplazarTodo(cargados);
                            System.out.println("Cargados " + cargados.size() + " productos.");
                        } else {
                            System.out.println("Operación cancelada.");
                        }
                    }
                    case 5 -> {
                        GestorXmlProductos.exportar(inventario.getProductos(), GestorXmlProductos.EXPORTACION);
                        System.out.println("Exportado a " + GestorXmlProductos.EXPORTACION + ".");
                    }
                    case 6, 7 -> {
                        String nombre = Funciones.leerTexto(teclado, "Archivo XML dentro de datos: ");
                        List<Producto> importados = GestorXmlProductos.importar(nombre);
                        if (opcion == 6) {
                            if (Funciones.confirmar(teclado, "Se sustituirán los datos por " + importados.size()
                                    + " productos. ¿Continuar?")) {
                                inventario.reemplazarTodo(importados);
                                System.out.println("Importación realizada.");
                            } else {
                                System.out.println("Operación cancelada.");
                            }
                        } else {
                            int anadidos = GestorXmlProductos.fusionar(inventario.getProductos(), importados);
                            System.out.println("Fusión completada: " + anadidos + " productos nuevos.");
                        }
                    }
                    case 8 -> System.out.println(GestorCopias.crearCopia()
                            ? "Copia creada." : "No hay CSV que copiar: guarda antes el inventario.");
                    case 9 -> {
                        if (!GestorCopias.hayCopia()) {
                            System.out.println("No existe ninguna copia de seguridad.");
                        } else if (Funciones.confirmar(teclado, "Se sustituirá el CSV actual por la copia. ¿Continuar?")) {
                            if (GestorCopias.restaurar()) {
                                inventario.reemplazarTodo(RepositorioCsvProductos.cargar());   // RECARGAR
                                System.out.println("Copia restaurada y datos recargados.");
                            }
                        } else {
                            System.out.println("Operación cancelada.");
                        }
                    }
                    case 0 -> System.out.println("Volviendo...");
                    default -> System.out.println("Opción no válida.");
                }
            } catch (IOException e) {
                System.out.println("Error: " + e.getMessage());
            }
        } while (opcion != 0);
    }

    // ---------------- SALIR CON PREGUNTA DE GUARDADO ----------------
    static void salir() {
        if (Funciones.confirmar(teclado, "¿Guardar el inventario en CSV antes de salir?")) {
            try {
                RepositorioCsvProductos.guardar(inventario.getProductos());
                System.out.println("Inventario guardado.");
            } catch (IOException e) {
                System.out.println("No se pudo guardar: " + e.getMessage());
            }
        }
        System.out.println("Hasta luego.");
    }
}

/*
======================================================================
[BUSCAR: ERRORES] - ERRORES TÍPICOS Y CHECKLIST FINAL
======================================================================
ERRORES QUE QUITAN PUNTOS:
 1. split(";") sin el -1  -> pierdes campos vacíos del final.
 2. No saltarse la cabecera (bucle desde i = 1) o NO escribirla al guardar.
 3. Reescribir el fichero cuando el ID NO existe (devolver false sin tocar nada).
 4. Hacer la copia o guardar ANTES de comprobar que el cambio es válido.
 5. Eliminar/modificar SIN crear copia antes (luego "restaurar" no recupera nada).
 6. ObjectOutputStream con APPEND (corrompe el .dat). Guardar la lista ENTERA.
 7. Leer un .dat sin comprobar instanceof List<?> y de cada elemento.
 8. System.out / Scanner dentro de las clases de datos (solo en Main).
 9. Modificar la lista principal ANTES de terminar de validar una importación.
10. Construir el XML concatenando Strings (el & rompe el XML): usar DOM.
11. Olvidar UTF-8 o no cerrar streams (usa try-with-resources).
12. Olvidar recargar la lista tras restaurar la copia.
13. Un NumberFormatException sin capturar cierra el programa.
14. parseInt para un precio con decimales: usa Double.parseDouble.
15. Comparar un objeto con un número (buscarPorId(id) == id): devuelve un
    OBJETO o null -> compara con null.
16. Usar variables sueltas (id, precio...) dentro de un método que solo
    recibe un objeto: usa nuevo.getId(), nuevo.getPrecio()...
17. Restos del ejemplo copiado (clase, getters, rutas, variables viejas).
18. Usar RandomAccessFile (PROHIBIDO).

COMPROBACIONES TÍPICAS (hazlas antes de entregar):
 - Arranca y lista los datos iniciales.
 - Buscar un ID que existe, uno que no existe y un texto no numérico.
 - Alta válida; alta con ID repetido / nombre vacío / negativos (rechazadas).
 - Modificar solo cambia ese registro; ID inexistente o valor negativo no tocan el fichero.
 - Eliminar con N conserva; con S elimina; restaurar recupera lo eliminado.
 - Reiniciar el programa: los cambios guardados siguen ahí.
 - XML: & como &amp; y tildes intactas; XML erróneo rechazado SIN perder datos.
 - Binario: cambiar y recargar SIN guardar descarta; guardar + reiniciar conserva.

ENTREGA: los .java y los datos generados (.csv, .dat, .bak, .xml). Sin .class.
======================================================================
*/