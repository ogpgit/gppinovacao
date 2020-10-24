# from gppinovacao.gppServicoPlanilha import abrir_planilha
from openpyxl import load_workbook



def test_int():
    assert 1 == 1


# def test_abrirPlanilha():
#    planilha = abrir_planilha('Contato.xlsx')
#    assert planilha.title == 'Plsan2'


def test_abrirPlanilha1():
    planilha = load_workbook('G:\AmbientePython\PycharmProjects\gppinovacao\Contato.xlsx').active
    #planilha = abrir_planilha('Contato.xlsx')
    assert planilha.title == 'Plan2'
