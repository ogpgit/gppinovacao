from openpyxl import Workbook, open, load_workbook


def abrir_planilha(nome_planilha):
    """
    Abrir uma planilha excel existente

    :param nome_planilha: str com o nome da planilha
    :return: um objeto workbook ativado
    """
    nome_planilha = f'G:\AmbientePython\PycharmProjects\gppinovacao\{nome_planilha}'

    return load_workbook(nome_planilha).active

def mostrar_conteudo_planilha(planilha):
    qtdeMaximaLinha = planilha.max_row
    qtdeMaximaColuna = planilha.max_column
    for i in range(1, qtdeMaximaLinha + 1):
        lista = []
        for j in range(1, qtdeMaximaColuna + 1):
            lista.append(planilha.cell(row=i, column=j).value)
        print(lista)
            # print(planilha.cell(row=i, column=j).value, end="\n")




if __name__ == '__main__':
    # abrir_planilha('Contato.xlsx') == 'Sucesso':
    planilha = abrir_planilha('Contato.xlsx')
    # planilha = abrir_planilha('gppInovacao.xlsx')

    # print(type(planilha))

    # mostrar o título da planilha
    print('\nTitulo da planilha')
    print(planilha.title)

    # mostrar conteudo da planilha
    print('\nMostrar conteudo da planilha')
    mostrar_conteudo_planilha(planilha)