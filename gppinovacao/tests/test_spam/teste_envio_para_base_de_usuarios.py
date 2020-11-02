from gppinovacao.spam.enviador_de_email import Enviador
from gppinovacao.spam.main import EnviadorDeSpam


def test_enviador_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'osvaldogpires@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantaticos'
    )
