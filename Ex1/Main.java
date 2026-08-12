package Ex1;

public class Main {
    public static void main(String[] args) {
        Livro livro = new Livro("El Principito");
        Usuario usuario = new Usuario("Itzel");

        Emprestimo emprestimo = new Emprestimo(usuario, livro);
        usuario.adicionarEmprestimo(emprestimo);
        livro.setDisponivel(false);

        System.out.println(usuario.getNome());
        System.out.println(usuario.getEmprestimos().size());
        System.out.println(livro.isDisponivel());
    }
}
