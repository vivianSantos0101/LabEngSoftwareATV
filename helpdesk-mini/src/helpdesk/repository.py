from .errors import ChamadoNaoEncontrado
from .models import Chamado


class ChamadoRepository:
    """Guarda chamados em memória. Não aplica regra de negócio."""

    def __init__(self) -> None:
        self._chamados: dict[int, Chamado] = {}
        self._proximo_id = 1

    def adicionar(self, chamado: Chamado) -> Chamado:
        chamado.id = self._proximo_id
        self._chamados[chamado.id] = chamado
        self._proximo_id += 1
        return chamado

    def buscar_por_id(self, chamado_id: int) -> Chamado:
        chamado = self._chamados.get(chamado_id)
        if chamado is None:
            raise ChamadoNaoEncontrado(f"Chamado {chamado_id} não encontrado.")
        return chamado

    def listar(self) -> list[Chamado]:
        return [self._chamados[i] for i in sorted(self._chamados)]
