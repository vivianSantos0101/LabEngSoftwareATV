package Ex4;

public class Pedido {
    private String status;

    public Pedido() {
        status = "Pendente";
    }

    public String getStatus() {
        return status;
    }

    public void atualizarStatus(String novoStatus) {
        status = novoStatus;
    }
}
