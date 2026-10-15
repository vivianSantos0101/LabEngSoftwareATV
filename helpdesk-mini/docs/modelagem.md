# Modelagem – HelpDesk Mini

## Diagrama de classes

```mermaid
classDiagram
    class Chamado {
        +int id
        +str titulo
        +str descricao
        +str solicitante
        +str prioridade
        +str status
        +str atendente
        +str solucao
        +str motivo_cancelamento
    }

    class ChamadoRepository {
        -dict _chamados
        -int _proximo_id
        +adicionar(chamado) Chamado
        +buscar_por_id(chamado_id) Chamado
        +listar() list~Chamado~
    }

    class ChamadoService {
        -ChamadoRepository _repositorio
        +abrir(titulo, descricao, solicitante, prioridade) Chamado
        +listar(status) list~Chamado~
        +buscar(chamado_id) Chamado
        +iniciar(chamado_id, atendente) Chamado
        +resolver(chamado_id, solucao) Chamado
        +cancelar(chamado_id, motivo) Chamado
    }

    class ValidacaoError
    class ChamadoNaoEncontrado
    class TransicaoInvalida
    class Exception

    Exception <|-- ValidacaoError
    Exception <|-- ChamadoNaoEncontrado
    Exception <|-- TransicaoInvalida

    ChamadoService --> ChamadoRepository : usa
    ChamadoRepository "1" o-- "*" Chamado : guarda
    ChamadoService ..> ValidacaoError : lança
    ChamadoService ..> ChamadoNaoEncontrado : lança
    ChamadoService ..> TransicaoInvalida : lança
```

## Tabela de transições

| Status atual | Operação | Status novo | Exige |
| --- | --- | --- | --- |
| `aberto` | iniciar | `em_andamento` | atendente válido |
| `em_andamento` | resolver | `resolvido` | solução válida |
| `aberto` | cancelar | `cancelado` | motivo válido |
| `em_andamento` | cancelar | `cancelado` | motivo válido |

Qualquer outra combinação gera `TransicaoInvalida` e o chamado não muda.
`resolvido` e `cancelado` são estados finais.

## Papel de cada classe

- **Chamado:** entidade que guarda os dados de um pedido de suporte e o seu status atual.
- **ChamadoRepository:** guarda os chamados em memória, gera o id sequencial e permite buscar e listar; não aplica regra de negócio.
- **ChamadoService:** ponto de entrada da aplicação; valida os campos, aplica a tabela de transições e usa o repositório.
- **ValidacaoError:** indica que algum campo informado está fora da regra.
- **ChamadoNaoEncontrado:** indica que o id buscado não existe no repositório.
- **TransicaoInvalida:** indica uma mudança de status que não está na tabela de transições.
