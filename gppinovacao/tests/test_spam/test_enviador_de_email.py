import pytest

from gppinovacao.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


remetente = 'osvaldogpires@gmail.com'


@pytest.mark.parametrize(
    'remetente',
    ['osvaldogpires@gmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'osvaldo-gp@detran.go.gov.br',
        'Cursos Python Pro',
        'Primeira turma do curso Python Pro'
    )
    assert remetente in resultado
