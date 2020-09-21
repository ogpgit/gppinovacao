from openpyxl import load_workbook


def abrir_planilha(nome_planilha):
    nome_planilha = f'G:\AmbientePython\PycharmProjects\gppinovacao\{nome_planilha}'
    return load_workbook(nome_planilha).active


if __name__ == '__main__':
    planilha = abrir_planilha('Contato.xlsx')
