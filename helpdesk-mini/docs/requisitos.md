# Requisitos – HelpDesk Mini

## História 1 – Abrir chamado

Como solicitante, quero abrir um chamado com prioridade
para que o laboratório saiba o que atender primeiro.

**Critério de aceite:** um chamado válido nasce com status `aberto`, id positivo
(o primeiro recebe id 1, o segundo id 2) e prioridade igual à informada.
Título com menos de 5 caracteres ou prioridade fora de `baixa`, `media` e `alta`
gera `ValidacaoError` e nenhum chamado é gravado.

## História 2 – Consultar a fila

Como solicitante, quero consultar a fila de chamados filtrando por status
para saber quais pedidos ainda estão esperando atendimento.

**Critério de aceite:** listar com `status="aberto"` devolve somente chamados abertos,
em ordem crescente de id. Buscar um id inexistente gera `ChamadoNaoEncontrado`.

## História 3 – Iniciar e resolver um chamado

Como atendente, quero iniciar e depois resolver um chamado
para registrar quem atendeu e qual foi a solução aplicada.

**Critério de aceite:** iniciar um chamado aberto grava o atendente e muda o status
para `em_andamento`; resolver um chamado em andamento grava a solução e muda o status
para `resolvido`. Resolver um chamado que ainda está aberto gera `TransicaoInvalida`.

## História 4 – Cancelar um chamado não encerrado

Como solicitante ou atendente, quero cancelar um chamado que ainda não foi encerrado
para tirar da fila pedidos que não fazem mais sentido.

**Critério de aceite:** um chamado `aberto` ou `em_andamento` pode ser cancelado com
motivo válido. Cancelar um chamado `resolvido` gera `TransicaoInvalida` e o status
permanece `resolvido`.
