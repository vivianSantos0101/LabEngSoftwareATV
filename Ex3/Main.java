package Ex3;

public class Main {
    public static void main(String[] args) {
        Aluno aluno = new Aluno("Juan Martin");

        aluno.adicionarNota(4.5);
        aluno.adicionarNota(7);

        System.out.println(aluno.media());
    }
}
