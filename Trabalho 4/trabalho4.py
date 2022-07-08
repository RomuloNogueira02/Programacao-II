import operator
import math
import itertools
import functools
import csv
import matplotlib.pyplot as plt
from datetime import datetime

__author__ = "Rómulo Nogueira, 56935"


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



def limpa_converte(dados, lista_colunas, pred_filtragem,funs_converter):
    """Função que limpa e converte os valores de determinados dados

    Args:
        dados (list[dict]): Lista de dicionários com os dados
        lista_colunas (list): Listas com as colunas que nos interessam
        pred_filtragem (function): Função a ser aplicada para filtrar os dados
        funs_converter (list): Lista de funções para converter os dados

    Returns:
        list[dict]: Lista de dicinários limpos e convertidos
    """
    novos_dados = [{chave:valor for chave,valor in linha.items() if chave in lista_colunas} for linha in dados]
    novos_dados_limpos = list(filter(pred_filtragem, novos_dados)) 
    lista_valores = list(map(lambda linha: list(linha.values()), novos_dados_limpos))
    lista_chaves = list(map(lambda linha: list(linha.keys()), novos_dados_limpos ))
    resultado = list(map(lambda linha: list(map(lambda x, fun: fun(x), linha, funs_converter)), lista_valores))
    final = list(map(lambda i: dict(zip(lista_chaves[i],resultado[i])), range(len(resultado))))
    return final




def media(lista): 
    """Função auxiliar que calcula a média de uma lista

    Args:
        lista (list): Lista que vai ser calculada a média

    Returns:
        float: Média dos valores da lista
    """
    return sum(lista) / len(lista)



def desvio_padrao_aux(lista):
    """Função auxiliar que calcula o desvio padrão de uma lista

    Args:
        lista (list): Lista que vai ser cálculada o desvio padrão

    Returns:
        float: Desvio padrão dos valores da lista
    """
    return math.sqrt(sum(map(lambda x: (x - media(lista))**2, lista)) / len(lista))
    


def media_movel(yy, janela):
    """Função que cálcula a média móvel das ordenadas de um conjunto de dados

    Args:
        yy (list): Lista das ordenadas do conjunto de dados
        janela (int): Valor que serve de janela temporal no cálculo da média movel

    Returns:
        list: Lista com os valores da média móvel cálculados
    """
    contador_primeiros, contador_sem_primeiros = list(range(1,janela)), list(range(len(yy) - janela + 1))
    primeiros = yy[:janela - 1]
    com_primeiros = list(map(lambda i: sum(primeiros[:i])/i , contador_primeiros))
    sem_primeiros = list(map(lambda i: media(yy[i:i+janela]), contador_sem_primeiros))
    return operator.concat(com_primeiros, sem_primeiros)


def desvio_padrao(yy, janela):
    """Função que cálcula o desvio padrão das ordenadas de um conjunto de dados

    Args:
        yy (list): Lista das ordenadas do conjunto de dados
        janela (int): Valor que serve de janela temporal no cálculo do desvio padrão

    Returns:
        list: Lista com os valores cálculados do desvio padrão
    """
    contador_primeiros, contador_sem_primeiros = list(range(1,janela)), list(range(len(yy) - janela + 1))
    primeiros = yy[:janela - 1]
    sem_primeiros = list(map(lambda i: desvio_padrao_aux(yy[i: i+janela]) ,contador_sem_primeiros))
    com_primeiros = list(map(lambda i: desvio_padrao_aux(primeiros[:i]) ,contador_primeiros))
    return operator.concat(com_primeiros, sem_primeiros)


def tracar(abcissas, ordenadas, parametros, janela=30):
    """Função que traça gráficos

    Args:
        abcissas (list): Lista das abcissas do gráfico
        ordenadas (list): Lista das ordenadas do gráfico
        parametros (dict): Dicionário com parâmetros para embelezar o gráfico
        janela (int, optional): Janela temporal na qual vai ser calculada. Defaults to 30.
    """
    plt.scatter(abcissas,ordenadas, s=parametros['TamanhoPontos'], c=parametros['CorPontos'])
    medio, desvio = media_movel(ordenadas, janela), list(map(lambda numero: 2 * numero, desvio_padrao(ordenadas, janela)))
    superior = list(map(lambda num1,num2: num1 + num2, medio, desvio))
    inferior = list(map(lambda num1,num2: num1 - num2, medio, desvio))
    plt.plot(abcissas, medio, color = parametros['CorLinha'] ,linewidth = parametros['Width'])
    plt.fill_between(abcissas, inferior, superior, alpha= parametros['Sombreado'])
    plt.xlabel(parametros['xLabel'])
    plt.ylabel(parametros['yLabel'], fontdict= parametros['Fonte'])
    plt.title(parametros['Titulo'])
    plt.show()



def sakura(ficheiro_csv):
    """Função que recebe um ficheiro csv (nomeadamente 'kyoto.csv') e traça
    o seu gráfico.

    Args:
        ficheiro_csv (str): Ficheiro csv ('kyoto.csv')
    """
    parametros_sakura = {'Titulo':'Registo Histórico da Data de Florescimento \n das Cerejeiras em Quioto', 'CorPontos': 'green', 'CorLinha': 'red', 'xLabel': 'Ano DC', 
                        'yLabel': 'Dias a partir do início do ano', 'Fonte': {'color': 'green'}, 'Width': '2', 'Sombreado': 0.2, 'TamanhoPontos': 1.5}
    ficheiro = ler_csv_dicionario(ficheiro_csv)
    ficheiro_limpo = limpa_converte(ficheiro, ['AD', 'Full-flowering date (DOY)'], lambda d: d['Full-flowering date (DOY)'] != '', [int, int])
    abcissas = list(map(lambda dic: dic['AD'], ficheiro_limpo))
    ordenadas = list(map(lambda dic: dic['Full-flowering date (DOY)'], ficheiro_limpo))
    tracar(abcissas,ordenadas,parametros_sakura)



def sismos(ficheiro_csv):
    """Função que recebe um ficheiro csv (nomeadamente 'all_month.csv') e traça
    o seu gráfico.
    
    Args:
        ficheiro_csv (str): Ficheiro csv ('all_month.csv')
    """
    parametros_sismos = {'Titulo':'Sismos no mês de Março', 'CorPontos': 'green', 'CorLinha': 'blue', 'xLabel': 'Minutos desde o inicio do mês', 
                        'yLabel': 'Média das magnitudes para cada minuto', 'Fonte': {'color': 'green'}, 'Width': '1', 'Sombreado': 0.3, 'TamanhoPontos': 0.2}
    ficheiro = ler_csv_dicionario(ficheiro_csv, delimitador=',')
    ficheiro_limpo = limpa_converte(ficheiro, ['time', 'mag'], lambda d: d['mag'] != '', [lambda tempo: datetime.strptime(tempo[:-5], "%Y-%m-%dT%H:%M:%S").strftime("%d %H %M"), float]) 
    abcissas_nao_convertidas = list(map(lambda dic: dic['time'], ficheiro_limpo))
    abcissas_convertidas = list(map(lambda x: (int(x[:2])*1440 + int(x[3:5])*60 + int(x[6:])) - 1440, abcissas_nao_convertidas))
    abcissas_com_mag = list(zip(abcissas_convertidas, list(map(lambda dic: dic['mag'], ficheiro_limpo))))
    ordenadas_sem_media = [list(map(lambda x: x[1], y)) for x,y in itertools.groupby(abcissas_com_mag, operator.itemgetter(0))]
    ordenadas = list(map(lambda linha: media(linha), ordenadas_sem_media))
    abcissas = [x for x,y in itertools.groupby(abcissas_com_mag, operator.itemgetter(0))]
    tracar(abcissas,ordenadas,parametros_sismos)


