from openpyxl import Workbook, open, load_workbook


def abrir_planilha(nome_planilha):
    """
    Editar e alterar uma planilha excel

    :param nome_planilha: str com o nome do arquivo excel
    :return: str de "sucesso" ou "cancelado"
    """
    nome_planilha = f'G:\AmbientePython\PycharmProjects\gppinovacao\{nome_planilha}'

    ws = load_workbook(nome_planilha,read_only=False)
    # ws = open(nome_planilha, read_only='n')

    # workbook = load_workbook('----------/dataset.xlsx')
    # sheet = workbook.active
    # row_count = sheet.max_row
    # for i in range(row_count):
    #    print(sheet.cell(row=i, column=2).value)
    sheet = ws.active
    row_count = sheet.max_row
    print(row_count)
    for i in range(row_count):
        print(i)
        print(sheet.cell(row=i + 1, column=1).value)



    return 'Sucesso'

if __name__ == '__main__':
    if abrir_planilha('Contato.xlsx') == 'Sucesso':
        print('hello')
    else:
        print('Arquivo não existe')