from .errors import TransicaoInvalida, ValidacaoError
from .models import (
    ABERTO,
    CANCELADO,
    EM_ANDAMENTO,
    PRIORIDADES,
    RESOLVIDO,
    STATUS,
    Chamado,
)
from .repository import ChamadoRepository

# (status atual, operação) -> status novo
TRANSICOES = {
    (ABERTO, "iniciar"): EM_ANDAMENTO,
    (EM_ANDAMENTO, "resolver"): RESOLVIDO,
    (ABERTO, "cancelar"): CANCELADO,
    (EM_ANDAMENTO, "cancelar"): CANCELADO,
}


def _texto(valor, campo: str, minimo: int, maximo: int | None = None) -> str:
    if not isinstance(valor, str):
        raise ValidacaoError(f"{campo} deve ser texto.")
    valor = valor.strip()
    if len(valor) < minimo:
        raise ValidacaoError(f"{campo} deve ter pelo menos {minimo} caracteres.")
    if maximo is not None and len(valor) > maximo:
        raise ValidacaoError(f"{campo} deve ter no máximo {maximo} caracteres.")
    return valor


class ChamadoService:
    """Regras de negócio do HelpDesk Mini: validação e transições de status."""

    def __init__(self, repositorio: ChamadoRepository | None = None) -> None:
        self._repositorio = repositorio or ChamadoRepository()

    def abrir(self, titulo, descricao, solicitante, prioridade) -> Chamado:
        titulo = _texto(titulo, "título", 5, 80)
        descricao = _texto(descricao, "descrição", 15, 400)
        solicitante = _texto(solicitante, "solicitante", 3, 80)
        if not isinstance(prioridade, str) or prioridade.strip() not in PRIORIDADES:
            raise ValidacaoError("prioridade deve ser baixa, media ou alta.")

        chamado = Chamado(titulo, descricao, solicitante, prioridade.strip())
        return self._repositorio.adicionar(chamado)

    def listar(self, status=None) -> list[Chamado]:
        chamados = self._repositorio.listar()
        if status is None:
            return chamados
        if status not in STATUS:
            raise ValidacaoError(f"status inválido: {status}.")
        return [c for c in chamados if c.status == status]

    def buscar(self, chamado_id) -> Chamado:
        return self._repositorio.buscar_por_id(chamado_id)

    def iniciar(self, chamado_id, atendente) -> Chamado:
        chamado = self.buscar(chamado_id)
        novo_status = self._proximo_status(chamado, "iniciar")
        atendente = _texto(atendente, "atendente", 3, 80)
        chamado.atendente = atendente
        chamado.status = novo_status
        return chamado

    def resolver(self, chamado_id, solucao) -> Chamado:
        chamado = self.buscar(chamado_id)
        novo_status = self._proximo_status(chamado, "resolver")
        solucao = _texto(solucao, "solução", 15)
        chamado.solucao = solucao
        chamado.status = novo_status
        return chamado

    def cancelar(self, chamado_id, motivo) -> Chamado:
        chamado = self.buscar(chamado_id)
        novo_status = self._proximo_status(chamado, "cancelar")
        motivo = _texto(motivo, "motivo", 10)
        chamado.motivo_cancelamento = motivo
        chamado.status = novo_status
        return chamado

    @staticmethod
    def _proximo_status(chamado: Chamado, operacao: str) -> str:
        novo = TRANSICOES.get((chamado.status, operacao))
        if novo is None:
            raise TransicaoInvalida(
                f"Não é possível {operacao} um chamado com status {chamado.status}."
            )
        return novo
