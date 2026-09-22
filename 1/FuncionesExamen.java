import java.util.ArrayList;
import java.util.Scanner;

public class FuncionesExamen {
  
    static boolean esTrabajoValido(String trabajo) {
        boolean resultado =
                trabajo.equals("arado") ||
                trabajo.equals("transporte") ||
                trabajo.equals("siembra");
        return resultado;
    }

     public static String leerTrabajoValido(Scanner scanner){
        String trabajo = "";
        boolean valido = false;

        while (!valido) {
            imprimirPrompt("Trabajo (arado/ transporte/ siembra)");
            trabajo = scanner.nextLine().trim().toLowerCase();
            valido = esTrabajoValido(trabajo);
            if (!valido) {
                imprimirMensaje("Trabajo no válido");
            }
        }
        return trabajo;
    }

    public static void aniadirTractor(Scanner scanner, ArrayList<String> marca, ArrayList<Integer> potencia, ArrayList<String> trabajo){
        imprimirPrompt("Marca del tractor: ");
        String nuevoTractor = scanner.nextLine().trim();
        marca.add(nuevoTractor);
        
        int nuevaPotencia = leerEnteroMayorQueCero(scanner, "Potencia (CV): ");
        potencia.add(nuevaPotencia);
        
        String nuevoTipoTrabajo = leerTrabajoValido(scanner);
        trabajo.add(nuevoTipoTrabajo);
    }

     static boolean terminaEnDigito(String texto) {
        boolean terminaEnNumero = false;

        if (texto.length() > 0) {
            char ultimo = texto.charAt(texto.length() - 1);
            terminaEnNumero = (ultimo >= '0' && ultimo <= '9');
        }

        return terminaEnNumero;
    }

    static boolean terminaEnPar(String texto) {
        boolean par = false;

        if (terminaEnDigito(texto)) {
            char ultimo = texto.charAt(texto.length() - 1);
            int numero = ultimo - '0';
            par = (numero % 2 == 0);
        }

        return par;
    }

    public static int leerEnteroMayorQueCero(Scanner scanner, String propmpt){
        int numero = 0;

        while (numero <= 0) {
            imprimirPrompt(propmpt);
            numero = leerEntero(scanner);
            if (numero <= 0) {
                imprimirMensaje("Debe ser mayor que 0.");
            }
        }
        return numero;
    }

      public static void listarTractores(ArrayList<String> marca, ArrayList<Integer> potencia, ArrayList<String> trabajo){
        if (marca.isEmpty()) {
            imprimirMensaje("No hay tractores");
        } else {
            int indice = 0;
            while (indice < marca.size()) {
                imprimirMensaje(indice + " -> Marca: " + marca.get(indice) + 
                                " | " + potencia.get(indice) +
                                "CV | trabajo: " + trabajo.get(indice));
                indice++;
            }
        }
    }

     public static int pedirIndiceValido(Scanner scanner, int tam, String propmpt){
            int indice = -1;

            while (indice < 0 || indice >= tam) {
                imprimirPrompt(propmpt);
                indice = leerEntero(scanner);
                if (indice < 0 || indice >= tam) {
                    imprimirMensaje("Indice fuera de rango");
                }
            }
            return indice;
    }    

    public static void eliminarTractor(Scanner scanner, ArrayList<String> marca, ArrayList<Integer> potencia, ArrayList<String> trabajo) {
        if (marca.isEmpty()) {
            imprimirMensaje("No hya tractores para eliminar");
        } else {
            listarTractores(marca, potencia, trabajo);
            int indice = pedirIndiceValido(scanner, marca.size(), "Índice a eliminar: ");
            marca.remove(indice);
            potencia.remove(indice);
            trabajo.remove(indice);
            imprimirMensaje("Tractor eliminado correctamente");
        }
    }

     public static void imprimirPrompt(String mensaje){
        System.out.println(mensaje);
    }

    public static int mostrarMenuYLeerOpcion(Scanner scanner, String menu){
        imprimirMensaje(menu);
        imprimirPrompt("Opción: ");
        int opcion = leerEntero(scanner);
        return opcion;
    }

     public static int leerEntero(Scanner scanner){
        int numero = 0;
        boolean numeroValido = false;

        while (!numeroValido) {
            String texto = scanner.nextLine().trim();
            try {
                numero = Integer.parseInt(texto);
                numeroValido = true;
            } catch (Exception e) {
                imprimirPrompt("Debes introducir un número entero: ");
            }
        }
        return numero;
    }


     public static boolean esNegativo(int n) {
        if (n < 0) {
            return true;
        } else {
            return false;
        }
    }


    public static boolean esPositivo(int n) {
        if (n > 0) {
            return true;
        } else {
            return false;
        }
    }


     public static boolean esImpar(int n) {
        if (n % 2 != 0) {
            return true;
        } else {
            return false;
        }
    }

      public static boolean esPar(int n) {
        if (n % 2 == 0) {
            return true;
        } else {
            return false;
        }
    }

    public static int contarVocales(String cadena) {
        int contador = 0;
        for (int i = 0; i < cadena.length(); i++) {
            char c = cadena.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                contador++;
            }
        }
        return contador;
    }

    public static int leerNumero(String mensaje, Scanner sc) {
        System.out.println(mensaje);
        int numero = sc.nextInt();
        sc.nextLine(); 
        return numero;
    }

    public static int contarImpares(ArrayList<Integer> array) {
        int contador = 0;
        for (int i = 0; i < array.size(); i++) {
            if (array.get(i) % 2 != 0) {
                contador++;
            }
        }
        return contador;
    }

     public static void imprimirArrayList(ArrayList<String> array) {
        for (int i = 0; i < array.size(); i++) {
            System.out.println(array.get(i));
        }
    }

    public static int numeroAleatorioEntreDosValores(int min, int max) {
        int resultado = (int) (Math.random() * (max - min + 1)) + min;
        return resultado;
    }

    public static ArrayList<Integer> invertirArrayList(ArrayList<Integer> array) {
        ArrayList<Integer> invertido = new ArrayList<>();
        for (int i = array.size() - 1; i >= 0; i--) {
            invertido.add(array.get(i));
        }
        return invertido;
    }

    public static int contarVocalesEnCadena(String cadenaTexto) {
        int cantidadVocales = 0;
        char caracterTexto;
        for (int i = 0; i < cadenaTexto.length(); i++) {
            caracterTexto = cadenaTexto.charAt(i);
            if (caracterTexto == 'a' || caracterTexto == 'e' || caracterTexto == 'i' || caracterTexto == 'o'
                    || caracterTexto == 'u') {
                cantidadVocales++;
            }
        }
        return cantidadVocales;
    }

    public static int valorMinimo(ArrayList<Integer> array) {
        if (array.size() == 0) {
            return 0;
        }

        int min = array.get(0);

        for (int i = 1; i < array.size(); i++) {
            if (array.get(i) < min) {
                min = array.get(i);
            }
        }

        return min;
    }

    public static int valorMaximo(ArrayList<Integer> array) {
        if (array.size() == 0) {
            return 0;
        }

        int max = array.get(0);

        for (int i = 1; i < array.size(); i++) {
            if (array.get(i) > max) {
                max = array.get(i);
            }
        }

        return max;
    }

    public static int sumarArray(ArrayList<Integer> array) {
        int suma = 0;
        for (int i = 0; i < array.size(); i++) {
            suma += array.get(i);
        }
        return suma;
    }

    public static ArrayList<Integer> filtrarNumeroMayores(ArrayList<Integer> arrayNumeros, int valor) {
        ArrayList<Integer> nuevoArray = new ArrayList<>();
        for (int i = 0; i < arrayNumeros.size(); i++) {
            if (arrayNumeros.get(i) > valor) {
                nuevoArray.add(arrayNumeros.get(i));
            }
        }
        return nuevoArray;
    }

    public static String capitalizarPrimeraLetra(String cadena) {
        String resultado = "";
        for (int i = 0; i < cadena.length(); i++) {
            if (i == 0) {
                resultado += Character.toUpperCase(cadena.charAt(i));
            } else {
                resultado += cadena.charAt(i);
            }
        }
        return resultado;
    }

    public static String revertirCadena(String cadena) {
        String ordenInverso = "";
        for (int i = cadena.length() - 1; i >= 0; i--) {
            ordenInverso += cadena.charAt(i);
        }
        return ordenInverso;
    }

    public static void numeroAleatorio() {
        int numero = (int) (Math.random() * 10);
        System.out.println("Número aleatorio: " + numero);
    }

    public static void aniadirSinDuplicados(String posibleDuplicado, ArrayList<String> array) {
        boolean duplicadosEncontrado = false;
        for (int i = 0; i < array.size() && !duplicadosEncontrado; i++) {
            if (array.get(i).equalsIgnoreCase(posibleDuplicado)) {
                duplicadosEncontrado = true;
            }
        }

        if (!duplicadosEncontrado) {
            array.add(posibleDuplicado);
        } else {
            imprimirMensaje("No se añade " + posibleDuplicado + " ya que está en el array");
        }
    }

    public static void leerStringArray(String mensajeString, ArrayList<String> array, Scanner sc) {
        String stringUsuario;
        imprimirMensaje(mensajeString);
        stringUsuario = sc.nextLine();
        aniadirSinDuplicados(stringUsuario, array);
    }

    public static void imprimirMensaje(String mensajeAMostrar) {
        System.out.println(mensajeAMostrar);
    }
}
