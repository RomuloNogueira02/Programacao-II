#!/usr/bin/env python

import operator
import itertools
import re
import csv
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

__author__ = "Rómulo Nogueira, 56935 ; Tiago Rosa, 56952"


def ler_csv_dicionario (nome_ficheiro, cabecalho = None , delimitador = ';'):
    """Função que lê um ficheiro csv transformando-o numa lista de dicionários

    Args:
        nome_ficheiro (str): Ficheiro csv a ser lido 
        cabecalho (list, optional): Lista com cabeçalho opcional. Defaults to None.
        delimitador (str, optional): Delimitador que separa as informações do ficheiro. Defaults to ';'.

    Returns:
        list[dict]: Lista de dicionários como conteúdo do ficheiro, as chaves por omissão
                    são os valores da primeira linha do ficheiro  
    """
    with open(nome_ficheiro, 'r', encoding='utf8') as ficheiro_csv:
        leitor = csv.DictReader(ficheiro_csv, fieldnames = cabecalho , delimiter = delimitador)
        return list(leitor)


######################################################################################################################################################################################################
#                                                                                     OPERAÇÃO ANOS                                                                                                  #
######################################################################################################################################################################################################

def anos(ficheiro_csv):
    """Desenha dois gráficos, um deles é um gráfico de barras com a o número de jogos, o outro é uma curva com o número de jogadoras

    Args:
        ficheiro_csv (str): Ficheiro csv a ser lido
    """
    leitor = ler_csv_dicionario(ficheiro_csv, delimitador= ',')
    ano = list(map(lambda linha: linha['end_time'][0:4], leitor))
    a = list(set(ano))
    ordenadas = list(map(lambda x: ano.count(x), sorted(a)))
    userWhite, userBlack = list(map(lambda linha: linha['white_username'], leitor)), list(map(lambda linha: linha['black_username'], leitor))
    novo = sorted((list(zip(ano, userWhite)) + list(zip(ano,userBlack))), key= operator.itemgetter(0))
    res = {chave: len(set(map(operator.itemgetter(1), valor))) for chave, valor in itertools.groupby(novo, operator.itemgetter(0))}
    
    _, grafico1 = plt.subplots()
    plt.xticks(rotation=90)
    plt.title("Jogos e jogadoras por ano")

    grafico1.set_xlabel("Ano")
    grafico1.set_ylabel("Jogos", color = "green")
    grafico1.bar(sorted(a), ordenadas, color="green", label = "#Jogos")
    grafico1.legend(loc = 'center left')

    grafico2 = grafico1.twinx()

    grafico2.set_ylabel("#Jogadoras diferentes", color = "blue")
    grafico2.plot(sorted(a), list(res.values()), color = "blue", label = "#jogadoras Diferentes")
    grafico2.legend(loc = 'upper left')
    grafico2.set_ylim(0, 12826)

    plt.show()


######################################################################################################################################################################################################
#                                                                                     OPERAÇÃO CLASSES                                                                                               #
######################################################################################################################################################################################################

dados = ler_csv_dicionario('xadrez.csv', delimitador=',')
lista_colunas = ['time_control', 'time_class']
funs_converter = [str,str]

def limpa_converte(dados, lista_colunas, pred_filtragem, funs_converter):
    """Função que limpa e converte os valores de determinados dados

    Args:
        dados (list[dict]): Lista de dicionários com os dados
        lista_colunas (list): Listas com as colunas que nos interessam
        pred_filtragem (function): Função a ser aplicada para filtrar os dados
        funs_converter (list): Lista de funções para converter os dados

    Returns:
        list[dict]: Lista de dicinários limpos e convertidos
    """
    filtrados = list(filter(pred_filtragem, dados))
    return list(map(lambda dic: (dict(map(lambda col, func: (col, func(dic[col])), lista_colunas, funs_converter))), filtrados))


pred_filtragem_600 = lambda d: d[lista_colunas[0]] == '600'

pred_filtragem_900 = lambda d: d[lista_colunas[0]] == '900'
pred_filtragem_900_10 = lambda d: d[lista_colunas[0]] == '900+10'
pred_filtragem_600_2 = lambda d: d[lista_colunas[0]] == '600+2'
pred_filtragem_900_5 = lambda d: d[lista_colunas[0]] == '900+5'
pred_filtragem_600_rapid = lambda d: d[lista_colunas[1]] == 'rapid'

pred_filtragem_1_259200 = lambda d: d[lista_colunas[0]] == '1/259200'
pred_filtragem_1_86400 = lambda d: d[lista_colunas[0]] == '1/86400'
pred_filtragem_1_1209600 = lambda d: d[lista_colunas[0]] == '1/1209600'
pred_filtragem_1_172800 = lambda d: d[lista_colunas[0]] == '1/172800'
pred_filtragem_1_432000 = lambda d: d[lista_colunas[0]] == '1/432000'

pred_filtragem_60 = lambda d: d[lista_colunas[0]] == '60'
pred_filtragem_60_1 = lambda d: d[lista_colunas[0]] == '60+1'
pred_filtragem_120_1 = lambda d: d[lista_colunas[0]] == '120+1'
pred_filtragem_120 = lambda d: d[lista_colunas[0]] == '120'
pred_filtragem_30 = lambda d: d[lista_colunas[0]] == '30'

pred_filtragem_180 = lambda d: d[lista_colunas[0]] == '180'
pred_filtragem_180_2 = lambda d: d[lista_colunas[0]] == '180+2'
pred_filtragem_180_1 = lambda d: d[lista_colunas[0]] == '180+1'
pred_filtragem_300 = lambda d: d[lista_colunas[0]] == '300'
pred_filtragem_600_blitz = lambda d: d[lista_colunas[1]] == 'blitz'

pred_filtragem_blitz = lambda d: d[lista_colunas[1]] == 'blitz'
pred_filtragem_rapid = lambda d: d[lista_colunas[1]] == 'rapid'
pred_filtragem_bullet = lambda d: d[lista_colunas[1]] == 'bullet'
pred_filtragem_daily = lambda d: d[lista_colunas[1]] == 'daily'


time_600 = limpa_converte(dados, lista_colunas, pred_filtragem_600, funs_converter)

# dados rapid
time_900 = len(limpa_converte(dados, lista_colunas, pred_filtragem_900, funs_converter))
time_900_10 = len(limpa_converte(dados, lista_colunas, pred_filtragem_900_10, funs_converter))
time_600_2 = len(limpa_converte(dados, lista_colunas, pred_filtragem_600_2, funs_converter))
time_900_5 = len(limpa_converte(dados, lista_colunas, pred_filtragem_900_5, funs_converter))
time_600_rapid = len(limpa_converte(time_600, lista_colunas, pred_filtragem_600_rapid, funs_converter))

# dados daily
time_1_259200 = len(limpa_converte(dados, lista_colunas, pred_filtragem_1_259200, funs_converter))
time_1_86400 = len(limpa_converte(dados, lista_colunas, pred_filtragem_1_86400, funs_converter))
time_1_1209600 = len(limpa_converte(dados, lista_colunas, pred_filtragem_1_1209600, funs_converter))
time_1_172800 = len(limpa_converte(dados, lista_colunas, pred_filtragem_1_172800, funs_converter))
time_1_432000 = len(limpa_converte(dados, lista_colunas, pred_filtragem_1_432000, funs_converter))

# dados bullet
time_60 = len(limpa_converte(dados, lista_colunas, pred_filtragem_60, funs_converter))
time_60_1 = len(limpa_converte(dados, lista_colunas, pred_filtragem_60_1, funs_converter))
time_120_1 = len(limpa_converte(dados, lista_colunas, pred_filtragem_120_1, funs_converter))
time_120 = len(limpa_converte(dados, lista_colunas, pred_filtragem_120, funs_converter))
time_30 = len(limpa_converte(dados, lista_colunas, pred_filtragem_30, funs_converter))

# dados blitz
time_180 = len(limpa_converte(dados, lista_colunas, pred_filtragem_180, funs_converter))
time_180_2 = len(limpa_converte(dados, lista_colunas, pred_filtragem_180_2, funs_converter))
time_180_1 = len(limpa_converte(dados, lista_colunas, pred_filtragem_180_1, funs_converter))
time_300 = len(limpa_converte(dados, lista_colunas, pred_filtragem_300, funs_converter))
time_600_blitz = len(limpa_converte(time_600, lista_colunas, pred_filtragem_600_blitz, funs_converter))

# dados time_class
daily = len(limpa_converte(dados, lista_colunas, pred_filtragem_daily, funs_converter))
bullet = len(limpa_converte(dados, lista_colunas, pred_filtragem_bullet, funs_converter))
rapid = len(limpa_converte(dados, lista_colunas, pred_filtragem_rapid, funs_converter))
blitz = len(limpa_converte(dados, lista_colunas, pred_filtragem_blitz, funs_converter))


def classes(quantidade = 5):
    """Desenha 4 gráficos que correspondem à quantidade de jogos dos vários tempos de jogo de cada time class.
       Desenha também o gráfico de comparação das time classes

    Args:
        quantidade (int, optional): quantidade de tempos de jogo em cada gráfico. Defaults to 5.
    """
    fig, ax = plt.subplots(2, 3)
    # grafico rapid
    xx_rapid = ['900', '900+10', '600+2', '900+5', '600']
    yy_rapid = [time_900, time_900_10, time_600_2, time_900_5, time_600_rapid]
    x_rapid = np.array(xx_rapid[:quantidade])
    y_rapid = np.array(yy_rapid[:quantidade])
    ax[0,0].bar(x_rapid,y_rapid)
    ax[0,0].set_title('rapid')
    ax[0,0].set_xlabel('Formato de jogo')
    ax[0,0].set_ylabel('#Jogos')
    ax[0,0].set_xticklabels(x_rapid, rotation=90)

    # grafico daily
    xx_daily = ['1/259200', '1/86400', '1/1209600', '1/172800', '1/432000']
    yy_daily = [time_1_259200, time_1_86400, time_1_1209600, time_1_172800, time_1_432000]
    x_daily = np.array(xx_daily[:quantidade])
    y_daily = np.array(yy_daily[:quantidade])
    ax[0,1].bar(x_daily,y_daily)
    ax[0,1].set_title('daily')
    ax[0,1].set_xlabel('Formato de jogo')
    ax[0,1].set_ylabel('#Jogos')
    ax[0,1].set_xticklabels(x_daily, rotation=90)

    #grafico bullet
    xx_bullet = ['60', '60+1', '120+1', '120', '30']
    yy_bullet = [time_60, time_60_1, time_120_1, time_120, time_30]
    x_bullet = np.array(xx_bullet[:quantidade])
    y_bullet = np.array(yy_bullet[:quantidade])
    ax[0,2].bar(x_bullet,y_bullet)
    ax[0,2].set_title('bullet')
    ax[0,2].set_xlabel('Formato de jogo')
    ax[0,2].set_ylabel('#Jogos')
    ax[0,2].set_xticklabels(x_bullet, rotation=90)

    # grafico blitz
    xx_blitz = ['180', '180+2', '180+1', '300', '600']
    yy_blitz = [time_180, time_180_2, time_180_1, time_300, time_600_blitz]
    x_blitz = np.array(xx_blitz[:quantidade])
    y_blitz = np.array(yy_blitz[:quantidade])
    ax[1,0].bar(x_blitz,y_blitz)
    ax[1,0].set_title('blitz')
    ax[1,0].set_xlabel('Formato de jogo')
    ax[1,0].set_ylabel('#Jogos')
    ax[1,0].set_xticklabels(x_blitz, rotation=90)

    #grafico time_class
    x_time_class = np.array(['blitz','bullet', 'daily', 'rapid'])
    y_time_class = np.array([blitz, bullet, daily, rapid])
    ax[1,1].bar(x_time_class,y_time_class)
    ax[1,1].set_title('time_class')
    ax[1,1].set_xlabel('Formato de jogo')
    ax[1,1].set_ylabel('#Jogos')
    ax[1,1].set_xticklabels(x_time_class, rotation=90)

    fig.delaxes(ax[1,2])
    fig.tight_layout()
    plt.show()



######################################################################################################################################################################################################
#                                                                                     OPERAÇÃO VITÓRIAS                                                                                              #
######################################################################################################################################################################################################

def vitorias(ficheiro, quantidade = 5, listaJogadoras = []):
    """Desenha um gráfico que representa a percentagem de vitórias de cada jogadora com as peças brancas e com as peças pretas

    Args:
        ficheiro (str): Ficheiro csv a ser lido
        quantidade (int, optional): Quantidade de jogadoras a mostrar os dados. Defaults to 5.
        listaJogadoras (list, optional): Lista de jogadoras caso queiramos comparar. Defaults to [].
    """
    leitor = ler_csv_dicionario(ficheiro, delimitador= ',')
    dados = list(map(lambda linha: [(linha['white_username'].lower()), linha['white_result'], (linha['black_username'].lower()), linha['black_result']], leitor))
    dados_filtrados = list(filter(lambda linha: linha[1] == 'win' or linha[3] == 'win' ,dados))
    vitorias_brancas = list(map(lambda linha: linha[0], filter(lambda linha: linha[1] == 'win' ,dados_filtrados)))
    vitorias_pretas = list(map(lambda linha: linha[2], filter(lambda linha: linha[3] == 'win' ,dados_filtrados)))
    vitorias = sorted(dict(Counter(vitorias_pretas + vitorias_brancas)).items(), key = operator.itemgetter(1), reverse= True)
    vit_brancas = dict(Counter(vitorias_brancas))
    vit_pretas = dict(Counter(vitorias_pretas))

    if listaJogadoras == []: 
        abcissas = list(map(lambda linha: linha[0], vitorias[:quantidade]))
    else: 
        abcissas = listaJogadoras

    jogosBrancos = list(map(lambda jogador: list(map(lambda linha: linha[0], dados_filtrados)).count(jogador) ,abcissas))
    jogosPretos = list(map(lambda jogador: list(map(lambda linha: linha[2], dados_filtrados)).count(jogador) ,abcissas))
    ordenadas_brancas = list(map(lambda jogadora,num: vit_brancas[jogadora] / num , abcissas, jogosBrancos))
    ordenadas_pretas =  list(map(lambda jogadora,num: vit_pretas[jogadora] / num , abcissas, jogosPretos))

    _, graficos = plt.subplots()
    grafico1 = graficos.bar(np.arange(len(abcissas)) - 0.4/2, ordenadas_brancas, width=0.4, color = "lightgray", label ="peças brancas")
    grafico2 = graficos.bar(np.arange(len(abcissas)) + 0.4/2, ordenadas_pretas, width=0.4, color = "black", label="peças pretas")
    graficos.legend(loc = 'upper right')

    graficos.set_xticks(range(len(abcissas)))
    graficos.set_xticklabels(abcissas)
    graficos.tick_params(axis='x', labelrotation = 90)
    graficos.set_title("Percentagem de vitórias jogando com \n peças brancas / pretas")
    graficos.set_ylabel("Perecentagem")
    graficos.set_xlabel("Jogadoras")
    plt.show()


######################################################################################################################################################################################################
#                                                                                     OPERAÇÃO SEGUINTE                                                                                              #
######################################################################################################################################################################################################

def seguinte(ficheiro_csv, elemento = 'e4', quantidade = 5):
    """Desenha um gráfico de barras com as jogadas mais prováveis após uma certa jogada

    Args:
        ficheiro_csv (str): Ficheiro csv a ser lido
        elemento (str, optional): Elemento do qual vão ser procuradas as jogadas mais prováveis a seguir . Defaults to 'e4'.
        quantidade (int, optional): Quantidade de jogadas a procurar. Defaults to 5.
    """
    leitor = ler_csv_dicionario(ficheiro_csv, delimitador= ',')
    dados = list(map(lambda linha: linha['pgn'], leitor))
    jogadas = list(filter(lambda linha: '{[%clk' in linha, dados))
    jogadas_sem_filtrar = list(map(lambda linha: re.findall(r'[a-zA-Z]+[0-9]{1}', linha), jogadas))
    jogadas_semi_filtradas = list(filter(lambda linha: elemento in linha[:-1], jogadas_sem_filtrar))
    jogadas_filtradas = list(filter(lambda linha: linha.index(elemento) == 0 , jogadas_semi_filtradas))
    seguidas = list(map(lambda linha: linha[1], jogadas_filtradas))
    infos = sorted(map(lambda x: (x, seguidas.count(x)), list(set(seguidas))), key=operator.itemgetter(1), reverse=True) 
    abcissas, ordenadas = list(map(lambda linha: linha[0], infos[:quantidade])), list(map(lambda linha: round(linha[1]/len(jogadas_filtradas),2), infos[:quantidade]))

    plt.bar(abcissas,ordenadas)
    plt.xlabel("Jogadas")
    plt.ylabel("Probabilidade")
    plt.title("Jogadas mais prováveis depois de " + elemento)

    plt.show()


######################################################################################################################################################################################################
#                                                                                     OPERAÇÃO MATE                                                                                                  #
######################################################################################################################################################################################################

def mate(ficheiro_csv, quantidade = 5):
    """Desenha dois gráficos em que um é um gráfico de barras que contém o número de jogos ganhos e o número de jogos ganhos por checkmate 
       e o outro é uma linha que mostra a percentagem de jogos ganhos por checkmate. 

    Args:
        ficheiro_csv (str): Ficheiro csv a ser lido 
        quantidade (int, optional): Quantidade de jogadoras a buscar os dados. Defaults to 5.
    """
    leitor = ler_csv_dicionario(ficheiro_csv, delimitador= ',')
    dados = list(map(lambda linha: [(linha['white_username'].lower()), linha['white_result'], (linha['black_username'].lower()), linha['black_result']], leitor))
    dados_filtrados = list(filter(lambda linha: linha[1] == 'win' or linha[3] == 'win' ,dados))
    vitorias_brancas = list(map(lambda linha: linha[0], filter(lambda linha: linha[1] == 'win' ,dados_filtrados)))
    vitorias_pretas = list(map(lambda linha: linha[2], filter(lambda linha: linha[3] == 'win' ,dados_filtrados)))
    vitorias = sorted(dict(Counter(vitorias_pretas + vitorias_brancas)).items(), key = operator.itemgetter(1), reverse= True)
    semi_checkmated = list(filter(lambda linha: 'checkmated' in linha,  dados_filtrados))
    checkmated_branco = list(map(lambda linha: linha[2] , filter(lambda linha: linha[1] == 'checkmated', semi_checkmated)))
    checkmated_preto = list(map(lambda linha: linha[0], filter(lambda linha: linha[3] == 'checkmated', semi_checkmated)))
    checkmates = dict(Counter(checkmated_branco + checkmated_preto))
    abcissas, ordenadas1 = list(map(lambda linha: linha[0], vitorias[:quantidade])) , list(map(lambda linha: linha[1], vitorias[:quantidade]))
    ordenadas2 = list(map(lambda jogadora: checkmates[jogadora], abcissas))
    percentagem_checkmate = list(map(lambda x,y: x/y, ordenadas2, ordenadas1))

    _, graficos = plt.subplots()
    grafico1 = graficos.bar(np.arange(len(abcissas)) - 0.4/2, ordenadas2, width=0.4, color = "lightgray", label ="jogos ganhos por xeque-mate")
    grafico2 = graficos.bar(np.arange(len(abcissas)) + 0.4/2, ordenadas1, width=0.4, color = "blue", label="jogos ganhos")
    graficos.legend(loc = 'upper right')

    graficos.set_xticks(range(len(abcissas)))
    graficos.set_xticklabels(abcissas)
    graficos.tick_params(axis='x', labelrotation = 90)
    graficos.set_title("Percentagem de xeque-mate, \n jogos ganhos, e jogos ganhos por xeque-mate")
    graficos.set_ylabel("#Jogos")

    grafico3 = graficos.twinx()

    grafico3.plot(abcissas, percentagem_checkmate, color="red", linewidth = '2', label= "percentagem \n de xeque-mate")
    grafico3.set_ylabel("Percentagem de xeque-mate" , color= "red")
    grafico3.legend(loc = 'center left')

    plt.show()


######################################################################################################################################################################################################
#                                                                                     OPERAÇÃO EXTRAIR                                                                                               #
######################################################################################################################################################################################################

def agrupar():
    """Associa cada linha do csv com o seu número de linha 

    Returns:
        list: Lista de tuplos ex: (1, linha 1)
    """
    return list(map(lambda num, dic: ((num+2), dic), list(range(len(ler_csv_dicionario('xadrez.csv', delimitador=',')))), ler_csv_dicionario('xadrez.csv', delimitador=',')))
        

def converter_agrupados(er, col):
    """Filtra os tuplos para que só estejam os da expressão regular numa certa coluna

    Args:
        er (str): Expressão regular
        col (str): Coluna a ser procurada

    Returns:
        list: Lista de tuplos filtrados
    """
    lista = agrupar()
    for tuplo in agrupar():
        if not re.search(er, tuplo[1][col]):
            lista.remove(tuplo)
    return lista



def extrair(ficheiro, output = 'out.csv', er = '.*', col = 'wgm_username'):
    """Extrai para um novo ficheiro csv as linhas que interessam ao utilizador

    Args:
        ficheiro (str): Ficheiro csv a ser lido
        output (str, optional): Nome do ficheiro de output. Defaults to 'out.csv'.
        er (str, optional): Expressão regular a ser procurada. Defaults to '.*'.
        col (str, optional): Coluna de interesse onde vai ser aplicada a expressão regular. Defaults to 'wgm_username'.
    """
    linhas = [num[0] for num in converter_agrupados(er, col)]
    with open(ficheiro, 'r') as reader: 
        with open (output, 'w') as writer:
            content = reader.readlines()
            writer.write("game_id,game_url,pgn,time_control,end_time,rated,time_class,rules,wgm_username,white_username,white_rating,white_result,black_username,black_rating,black_result\n")
            for linha in linhas:
                writer.write(content[linha-1]) 



######################################################################################################################################################################################################
#                                                                                PARA FUNCIONAR NO TERMINAL                                                                                          #
######################################################################################################################################################################################################


if __name__ == "__main__":
    import sys, argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('ficheiro', nargs='+' ,help='Ficheiro csv')
    
    parser.add_argument('-c' , 
                        type = int, 
                        default = 5,
                        nargs= '?',
                        help="PARA FUNCAO VITORIAS E PARA A FUNCAO SEGUINTES E FUNÇÃO MATE")
    parser.add_argument('-j' , 
                        type = str,
                        default= 'e4', 
                        nargs= '?',
                        help="PARA A FUNCAO SEGUINTES")
    parser.add_argument('-o', 
                        type = str,
                        default = 'out.csv',
                        nargs= '?',
                        help = 'nome de output do novo ficheiro csv')

    parser.add_argument('-r', 
                        type = str,
                        default= '.*',
                        nargs= '?',
                        help = 'expressao regular')

    parser.add_argument('-d',
                        type = str,
                        default= 'wgm_username',
                        nargs= '?',
                        help = 'coluna onde vai ser executada a expressao regular')
    parser.add_argument('-u',
                        nargs= '+',
                        help = 'coluna onde vai ser executada a expressao regular')

    arguments = parser.parse_args()

    if sys.argv[2] == 'anos':
        anos(arguments.ficheiro[0])

    if sys.argv[2] == 'classes':
        classes(quantidade = arguments.c)

    if sys.argv[2] == 'vitorias':
        if '-c' in sys.argv and '-u' in sys.argv:
            print("Os dois comandos não podem ser usados em simultâneo")
        else:
            if arguments.u == None: 
                jogadoras = []
            else:
                jogadoras = arguments.u
            vitorias(arguments.ficheiro[0], quantidade = arguments.c, listaJogadoras = jogadoras)

    if sys.argv[2] == 'seguinte':
        seguinte(arguments.ficheiro[0], elemento= arguments.j, quantidade = arguments.c)

    if sys.argv[2] == 'mate':
        mate(arguments.ficheiro[0], quantidade= arguments.c)

    if sys.argv[2] == 'extrair':
        extrair(arguments.ficheiro[0], output = arguments.o, er = arguments.r, col = arguments.d)
    