package Ex2;

public class Main {
    public static void main(String[] args) {
        Produto produto = new Produto("Mango", 8.0);
        ItemPedido item0 = new ItemPedido(produto, 5);

        Produto produto1 = new Produto("Piña", 6.5);
        ItemPedido item1 = new ItemPedido (produto1,3);

        Produto produto2 = new Produto("Limón", 3.5);
        ItemPedido item2 = new ItemPedido (produto2,2);


        System.out.println(item0.subtotal());
        System.out.println(item1.subtotal());
        System.out.println(item2.subtotal());
    }
}
