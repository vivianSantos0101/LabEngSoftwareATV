from dataclasses import dataclass

PRIORIDADES = ("baixa", "media", "alta")

ABERTO = "aberto"
EM_ANDAMENTO = "em_andamento"
RESOLVIDO = "resolvido"
CANCELADO = "cancelado"

STATUS = (ABERTO, EM_ANDAMENTO, RESOLVIDO, CANCELADO)


@dataclass
class Chamado:
    titulo: str
    descricao: str
    solicitante: str
    prioridade: str
    id: int = 0
    status: str = ABERTO
    atendente: str = ""
    solucao: str = ""
    motivo_cancelamento: str = ""
