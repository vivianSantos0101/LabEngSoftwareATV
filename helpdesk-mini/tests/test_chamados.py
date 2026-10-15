import pytest

from helpdesk import (
    ChamadoNaoEncontrado,
    ChamadoService,
    TransicaoInvalida,
    ValidacaoError,
)


@pytest.fixture
def service():
    return ChamadoService()


def abrir_valido(service, titulo="Projetor da sala 2"):
    return service.abrir(
        titulo,
        "A lampada nao acende durante a aula.",
        "Ana Souza",
        "alta",
    )


def test_abrir_chamado_valido_cria_id_1_e_status_aberto(service):
    chamado = abrir_valido(service)

    assert chamado.id == 1
    assert chamado.status == "aberto"
    assert chamado.prioridade == "alta"
    assert chamado.atendente == ""
    assert chamado.solucao == ""


def test_segundo_chamado_recebe_id_2(service):
    abrir_valido(service)
    segundo = abrir_valido(service, "Computador 7 travando")

    assert segundo.id == 2


def test_titulo_curto_gera_validacao_error_e_lista_vazia(service):
    with pytest.raises(ValidacaoError):
        service.abrir("PC", "A maquina nao liga de jeito nenhum.", "Ana Souza", "baixa")

    assert service.listar() == []


def test_prioridade_invalida_gera_validacao_error(service):
    with pytest.raises(ValidacaoError):
        service.abrir(
            "Projetor da sala 2",
            "A lampada nao acende durante a aula.",
            "Ana Souza",
            "urgente",
        )


def test_buscar_id_inexistente_gera_chamado_nao_encontrado(service):
    with pytest.raises(ChamadoNaoEncontrado):
        service.buscar(99)


def test_iniciar_chamado_aberto_grava_atendente_e_muda_status(service):
    chamado = abrir_valido(service)

    service.iniciar(chamado.id, "Carlos Lima")

    atualizado = service.buscar(chamado.id)
    assert atualizado.atendente == "Carlos Lima"
    assert atualizado.status == "em_andamento"


def test_resolver_chamado_aberto_gera_transicao_invalida(service):
    chamado = abrir_valido(service)

    with pytest.raises(TransicaoInvalida):
        service.resolver(chamado.id, "Lampada substituida e teste de imagem ok.")

    assert service.buscar(chamado.id).status == "aberto"


def test_resolver_chamado_em_andamento_grava_solucao_e_muda_status(service):
    chamado = abrir_valido(service)
    service.iniciar(chamado.id, "Carlos Lima")

    service.resolver(chamado.id, "Lampada substituida e teste de imagem ok.")

    atualizado = service.buscar(chamado.id)
    assert atualizado.solucao == "Lampada substituida e teste de imagem ok."
    assert atualizado.status == "resolvido"


def test_cancelar_chamado_resolvido_gera_transicao_invalida(service):
    chamado = abrir_valido(service)
    service.iniciar(chamado.id, "Carlos Lima")
    service.resolver(chamado.id, "Lampada substituida e teste de imagem ok.")

    with pytest.raises(TransicaoInvalida):
        service.cancelar(chamado.id, "Aberto por engano pelo aluno.")

    assert service.buscar(chamado.id).status == "resolvido"


def test_listar_por_status_aberto_devolve_so_abertos_em_ordem(service):
    primeiro = abrir_valido(service, "Projetor da sala 2")
    segundo = abrir_valido(service, "Computador 7 travando")
    terceiro = abrir_valido(service, "Impressora sem toner")
    service.iniciar(segundo.id, "Carlos Lima")

    abertos = service.listar(status="aberto")

    assert [c.id for c in abertos] == [primeiro.id, terceiro.id]
    assert all(c.status == "aberto" for c in abertos)
