package UD4.Ejercicios;

import java.util.Scanner;

public class PT1 {
    public static void main(String[] args) {
        final int ARROZMAKI = 120, ARROZNIGIRI = 50, ARROZSASHIMI = 0;
        final double AGUAMAKI = 0.1, AGUANIGIRI = 0.05, AGUASASHIMI = 0.02;
        final int PRECIOMAKI = 8, PRECIONIGIRI = 10, PRECIOSASHIMI = 12;

        Scanner scanner = new Scanner(System.in);
        int arrozGastadoAcumulado = 0, importe = 0, arrozGastadoPedido = 0;
        double aguaGastadaAcumulada = 0, aguaGastadoPedido;
        String tipoPlato = "";
        int contadorPedidos = 0;
        int totalPiezasMaki = 0, totalPiezasNigiri = 0, totalPiezasSashimi = 0;
        int arrozRestante = 0;
        double aguaRestante, stockAgua;
        int importeCajaTotal = 0;
        boolean stockSuperado = false;
        int numeroPedidos, stockArroz, unidades;

        System.out.println("Número de pedidos: ");
        numeroPedidos = scanner.nextInt();

        while (numeroPedidos <= 0) {
            System.out.println("Número de pedidos: ");
            numeroPedidos = scanner.nextInt();
        }

        System.out.println("Stock de arroz (g): ");
        stockArroz = scanner.nextInt();

        while (stockArroz <= 0) {
            System.out.println("Stock de arroz (g): ");
            stockArroz = scanner.nextInt();
        }

        System.out.println("Stock de agua (L): ");
        stockAgua = scanner.nextDouble();

        while (stockAgua <= 0) {
            System.out.println("Stock de agua (L): ");
            stockAgua = scanner.nextDouble();
        }

        for (int i = 1; i <= numeroPedidos && !stockSuperado; i++) {
            System.out.println("--- Pedido " + i + " ---");
            System.out.println("Tipo de plato (maki/nigiri/sashimi)".toLowerCase());
            tipoPlato = scanner.next();

            while (!tipoPlato.equals("maki") && !tipoPlato.equals("nigiri") && !tipoPlato.equals("sashimi")) {
                System.out.println("Tipo de plato (maki/nigiri/sashimi)".toLowerCase());
                tipoPlato = scanner.next();
            }

            System.out.println("Unidades: ");
            unidades = scanner.nextInt();

            while (unidades < 0) {
                unidades = scanner.nextInt();
            }

            if (tipoPlato.equals("maki")) {
                arrozGastadoPedido = ARROZMAKI * unidades;
                aguaGastadoPedido = AGUAMAKI * unidades;
                importe = PRECIOMAKI * unidades;

            } else if (tipoPlato.equals("nigiri")) {
                arrozGastadoPedido = ARROZNIGIRI * unidades;
                aguaGastadoPedido = AGUANIGIRI * unidades;
                importe = PRECIONIGIRI * unidades;

            } else {
                arrozGastadoPedido = ARROZSASHIMI * unidades;
                aguaGastadoPedido = AGUASASHIMI * unidades;
                importe = PRECIOSASHIMI * unidades;
            }

            if (stockArroz < arrozGastadoAcumulado + arrozGastadoPedido) {
                System.out.println("¡Alerta! Has superado el stock de arroz");
                stockSuperado = true;
            }

            if (stockAgua < aguaGastadaAcumulada + aguaGastadoPedido) {
                System.out.println("¡Alerta! Has superado el stock de agua");
                stockSuperado = true;
            }

            if (!stockSuperado) {
                contadorPedidos++;
                arrozGastadoAcumulado += arrozGastadoPedido;
                aguaGastadaAcumulada += aguaGastadoPedido;
                importeCajaTotal += importe;

                if (tipoPlato.equals("maki")) {
                    totalPiezasMaki += unidades;
                } else if (tipoPlato.equals("nigiri")) {
                    totalPiezasNigiri += unidades;
                } else {
                    totalPiezasSashimi += unidades;
                }

                System.out.println(
                        "Plato: " + tipoPlato + " | Unidades: " + unidades + " | Importe cobrado: " + importe + " €");
                System.out.println("Arroz gastado en el pedido: " + arrozGastadoPedido + "g | Arroz acumulado: "
                        + arrozGastadoAcumulado + "g");
                System.out.printf("Agua gastado en el pedido (L): %.2f | Agua acumulada (L): %.2f", aguaGastadoPedido,
                        aguaGastadaAcumulada);
            }
        }

        arrozRestante = stockArroz - arrozGastadoAcumulado;
        aguaRestante = stockAgua - aguaGastadaAcumulada;

        System.out.println("=== RESUMEN FINAL ===");
        System.out.println("Pedidos registrados: " + contadorPedidos + " de " + numeroPedidos);
        System.out.println("Unidades Maki: " + totalPiezasMaki + " | Nigiri: " + totalPiezasNigiri + " | Sashismi: "
                + totalPiezasSashimi);
        System.out
                .println("Consumo total Arroz: " + arrozGastadoAcumulado + " g | Agua: " + aguaGastadaAcumulada + " L");
        System.out.println("Stock restante Arroz: " + arrozRestante + " g | Agua: " + aguaRestante + " L");
        System.out.println("Caja del día: " + importeCajaTotal + " €");

        if (stockSuperado) {
            System.out.println("Mensaje final: Registro interrumpido por superación de stock");
        } else {
            System.out.println("Mensaje final: Registro completado con éxito");
        }

        scanner.close();
    }
}
