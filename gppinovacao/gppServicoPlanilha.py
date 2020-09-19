from openpyxl import Workbook, open, load_workbook


def abrir_planilha(nome_planilha):
    """
    Abrir uma planilha excel existente

    :param nome_planilha: str com o nome da planilha
    :return: um objeto workbook ativado
    """
    nome_planilha = f'G:\AmbientePython\PycharmProjects\gppinovacao\{nome_planilha}'

    return load_workbook(nome_planilha).active

if __name__ == '__main__':
    # abrir_planilha('Contato.xlsx') == 'Sucesso':
    planilha = abrir_planilha('Contato.xlsx')
    # planilha = abrir_planilha('gppInovacao.xlsx')

    # print(type(planilha))

    # mostrar o título da planilha
    print(planilha.title)