package  Ex1;

import java.util.ArrayList;
import java.util.List;

public class Usuario {
    private String nome;
    private List<Emprestimo> emprestimos;

    public Usuario(String nome) {
        this.nome = nome;
        this.emprestimos = new ArrayList<>();
    }

    public String getNome() {
        return nome;
    }

    public List<Emprestimo> getEmprestimos() {
        return emprestimos;
    }

    public void adicionarEmprestimo(Emprestimo emprestimo) {
        emprestimos.add(emprestimo);
    }
}
