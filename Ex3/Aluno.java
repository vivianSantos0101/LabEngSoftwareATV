package Ex3;

import java.util.ArrayList;
import java.util.List;

public class Aluno {
    private String nome;
    private List<Double> notas;

    public Aluno(String nome) {
        this.nome = nome;
        this.notas = new ArrayList<>();
    }

    public void adicionarNota(double nota) {
        notas.add(nota);
    }

    public double media() {
        if (notas.isEmpty()) {
            return 0;
        }

        double soma = 0;

        for (double nota : notas) {
            soma += nota;
        }

        return soma / notas.size();
    }
}
