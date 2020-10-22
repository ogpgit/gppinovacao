from gppinovacao.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'osvaldogpires@gmail.com',
        'osvaldo-gp@detran.go.gov.br',
        'Cursos Python Pro',
        'Primeira turma do curso Python Pro'
    )
    assert 'osvaldogpires@gmail.com' in resultado
