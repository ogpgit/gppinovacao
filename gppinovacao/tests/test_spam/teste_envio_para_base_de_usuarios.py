import pytest

from gppinovacao.spam.enviador_de_email import Enviador
from gppinovacao.spam.main import EnviadorDeSpam
from gppinovacao.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Osvaldo', email='osvaldogpires@gmail.com'),
            Usuario(nome='Silvia', email='osvaldogpires@gmail.com')
        ],
        [
            Usuario(nome='Osvaldo', email='osvaldogpires@gmail.com')
        ]
    ]
)
def test_qtde_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'osvaldogpires@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantaticos'
    )
    assert len(usuarios) == enviador.qtde_email_enviados


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtde_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtde_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Osvaldo', email='osvaldogpires@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'silvia1875@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantaticos'
    )
    assert enviador.parametros_de_envio == (
        'silvia1875@gmail.com',
        'osvaldogpires@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantaticos'
    )
