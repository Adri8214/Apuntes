package UD5.RelacionEjercicios1;

public class Ejercicio6 {
    public static void main(String[] args) {
       Reloj r1 = new Reloj(8, 45, 5);
       System.out.println(r1); 
    }
}

class Reloj{
    int hora;
    int minuto;
    int segundo;

    public Reloj(int hora, int minuto, int segundo){
        this.hora = hora;
        this.minuto = minuto;
        this.segundo = segundo;
    }

    public String toString() {
        return String.format("%02d:%02d:%02d", hora, minuto, segundo);
    }
}