class ValidacaoError(Exception):
    """Campo fora da regra."""


class ChamadoNaoEncontrado(Exception):
    """Id inexistente no repositório."""


class TransicaoInvalida(Exception):
    """Mudança de status fora da tabela de transições."""
