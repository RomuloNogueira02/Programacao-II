__author__ = "Rómulo Nogueira, 56935"

def ler_palavras(nome_ficheiro):
    """Função que recebe um ficheiro.txt e devolve um conjunto com as palavras
    que o ficheiro contém, excluindo repetições.    

    Args:
        nome_ficheiro (str): Ficheiro que recebemos com as palavras

    Returns:
        set : Conjunto com as palvras do ficheiro, sem conter palavras repetidas
    """
    listaConjunto = []
    conjunto = set()
    with open(nome_ficheiro, 'r', encoding='utf8') as ficheiro_leitura:
        ficheiro_leitura = ficheiro_leitura.read().split()
        for palavra in ficheiro_leitura:
            if palavra not in listaConjunto:
                listaConjunto.append(palavra)
                conjunto = set(sorted(listaConjunto))
        return conjunto


def contadores(nome_ficheiro, palavra):
    """Função que retorna a informação necessária para construir o dicionário na
    função a seguir, ou seja, em tuplo as vezes em que a palavra aparece no ficheiro 
    e as linhas em que aparece.

    Args:
        nome_ficheiro (str): Ficheiro dado pelo utilizador
        palavra (str): Palavra dada pelo utilizador para verificar se estão no ficheiro 

    Returns:
        tuple : tuplo que contém o numero de vezes que a palavra aparece no ficheiro
            e as linhas em que aparece.
    """
    lista_contadores = []
    conjunto = set()
    with open(nome_ficheiro, 'r', encoding='utf8') as ficheiro_texto:
        for contador,linha in enumerate(ficheiro_texto,1): # percorrer linhas e enumera-las a partir de 1
            if palavra in linha.split():
                lista_contadores.append(contador)
                conjunto = set(lista_contadores)
    return (len(lista_contadores),conjunto)

def encontrar_palavras(ficheiro1,ficheiro2):
    """Função que recebe dois ficheiros e devolve um dicionário
    que diz as vezes em que uma palavra de um dos ficheiros aparece  no outro 
    e ainda diz as linhas em que aparecem.

    Args:
        ficheiro1 (str): Ficheiro onde vão se procurar as palavras
        ficheiro2 (str): Ficheiro com as palavras a procurar

    Returns:
        dic: Dicionário com a palavra e as ocorrencias da mesma no ficheiro1 em 
        forma de tuplo, que contém o número de vezes que uma certa palavra aparece
        num ficheiro e as linhas em que aparece
    """
    palavras = ler_palavras(ficheiro2)
    lista_tuplos = []
    for palavra in palavras:
        lista_tuplos.append(contadores(ficheiro1,palavra))
    print(lista_tuplos)
    baseDeDados = [(x,y) for (x,y) in zip(palavras, lista_tuplos)]

    dicionario = {}
    for palavra,tuplo in baseDeDados:
        if palavra not in dicionario:
            dicionario[palavra] = tuplo
        else:
            dicionario[palavra] = dicionario[palavra] + tuplo
    return dicionario

