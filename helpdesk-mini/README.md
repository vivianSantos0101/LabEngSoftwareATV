# HelpDesk Mini

**Aluna:** [SEU NOME COMPLETO]
**Disciplina:** Laboratório de Engenharia de Software – Prof. Juan Hassam
**Atividade:** Reposição das aulas de 14/09/2026 e 16/09/2026

## O que é

O HelpDesk Mini é o núcleo de controle de chamados do laboratório de informática da universidade.
Ele substitui a planilha usada hoje e permite abrir um chamado com título, descrição, solicitante
e prioridade, acompanhar a fila filtrando por status, iniciar o atendimento, resolver ou cancelar,
sempre respeitando uma tabela fixa de transições de status. Os dados ficam em memória enquanto o
processo está rodando.

## Estrutura de pastas

```text
helpdesk-mini/
  README.md            documentação da entrega
  requirements.txt     dependências (pytest)
  pytest.ini           configura o pytest para achar o pacote em src/
  docs/
    requisitos.md      histórias de usuário e critérios de aceite
    modelagem.md       diagrama de classes (Mermaid) e tabela de transições
  src/
    helpdesk/
      models.py        entidade Chamado, prioridades e status
      errors.py        ValidacaoError, ChamadoNaoEncontrado e TransicaoInvalida
      repository.py    armazenamento em memória (adicionar, buscar_por_id, listar)
      service.py       ChamadoService: validação de campos e transições de status
  tests/
    test_chamados.py   os 10 cenários obrigatórios
```

## Como rodar

```bash
cd helpdesk-mini
python -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

Resultado esperado: `10 passed`.

## Decisões de projeto

A validação mora inteira no `ChamadoService`: cada texto passa por `strip` e é conferido
contra o tamanho mínimo e máximo antes de qualquer gravação, então um campo inválido
lança `ValidacaoError` sem tocar no repositório.
A transição de status também mora no serviço, em um dicionário `TRANSICOES` que mapeia
(status atual, operação) para o status novo; o que não está no dicionário gera `TransicaoInvalida`.
Em `iniciar`, `resolver` e `cancelar`, o serviço primeiro confere a transição, depois valida
o campo e só no final altera o chamado, para que um erro nunca deixe o chamado pela metade.
O repositório só guarda e recupera: mantém um dicionário em memória, gera o id sequencial
começando em 1, busca por id (lançando `ChamadoNaoEncontrado` se não existir) e lista em ordem de id.
Os testes usam apenas a interface pública do `ChamadoService`, sem acessar o dicionário interno.
