package Ex3;

public class AlunoTest {
    public static void main(String[] args) {
        Aluno aluno = new Aluno("Vivian");

        aluno.adicionarNota(8);
        aluno.adicionarNota(10);

        double resultado = aluno.media();

        if (resultado == 9) {
            System.out.println("Teste passou");
        } else {
            System.out.println("Teste falhou");
        }

        Aluno alunoSemNotas = new Aluno("Teste");

        if (alunoSemNotas.media() == 0) {
            System.out.println("Teste de lista vazia passou");
        } else {
            System.out.println("Teste de lista vazia falhou");
        }
    }
}
