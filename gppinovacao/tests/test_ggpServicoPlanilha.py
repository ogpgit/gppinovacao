from gppinovacao.gppServicoPlanilha import abrir_planilha


def test_int():
    assert 1 == 1


def test_abrirPlanilha():
    planilha = abrir_planilha('Contato.xlsx')
    assert type(planilha) != "<class 'openpyxl.worksheet.worksheet.Worksheet'>"
