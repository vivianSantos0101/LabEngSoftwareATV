package Ex4;

public class Main {
    public static void main(String[] args) {
        Pedido pedido = new Pedido();

        System.out.println(pedido.getStatus());

        pedido.atualizarStatus("Enviado");

        System.out.println(pedido.getStatus());
    }
}
