from gppinovacao.spam.db import Conexao
from gppinovacao.spam.modelos import Usuario


def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Osvaldo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuarios():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Osvaldo'), Usuario(nome='Silvia')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar_usuarios()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
