from openpyxl import Workbook


def abrirPlanilha(nomePlanilha):
    """
    Abrir uma planilha de trabalho e, caso não exista, dar a opção para que seja criada uma nova planilha

    :param planilhaName: str com o nome da planilha a ser aberta ou criada
    :return: um objeto WookBook
    """
    """
       Editar e alterar uma planilha excel

       :param arquivo: str com o nome do arquivo excel
       :return: str de "sucesso" ou "cancelado"

       """
    nomePlanilha = f'G:\AmbientePython\PycharmProjects\{nomePlanilha}'

    ws = Workbook()

    ws1 = open(nomePlanilha)
    print(type(ws1))

    return 'Sucesso'


if __name__ == '__main__':
    if abrirPlanilha('gppInovacao.xlsx') == 'Sucesso':
        print('hello')
    else:
        print('Arquivo não existe')

