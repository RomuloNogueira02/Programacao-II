
def f1(n, v):
    b = n * n
    s = 0
    while b > 1:  # O((n^2 - 1) / 2) = O(n^2)
        s+= v[n]
        s += b
        b -= 2
    return s

# 2 -> O(1) - pois guardar uma numa variável a multiplicação entre dois números (n) custa 1
# 3 -> O(1) - pois guardar o zero numa variável custa 1
# 4 -> O((n^2 - 1)/2) = O (n^2) - visto que o ciclo vai correr n^2 vezes até 1 subtraindo por 2 sucessivamente o valor do b, fica O(n^2) 
#                       porque o "-1" e a divisão acabam por ser irrelevantes 
# 5 -> O(1) - como n é um valor constante o acesso indexado custa 1 assim como guardar esse valor numa variável
# 6 -> O(1) - porque guardar numa variável a soma entre dois números custa 1 
# 7 -> O(1) - porque guardar numa variável a subtração entre dois números custa 1
# 8 -> O(1) - pois o return do valor de uma variável custa 1 
# Assim a função tem complexidade O(n^2) e é polinomial.


def f2(d,l):
    r = []
    for x in l:
        if x not in d:
            r.append(x)
    return r

d = {10:'um' ,62:'ola' ,4:'sou','ola':'2',6:'bom dia'}
l = [1,2,3,5,12]

print(f2(d,l))

# n = len(l)
# m = len(d)

# 2 -> O(1) - pois guardar numa variável a lista vazia custa 1
# 3 -> O(n) - pois o ciclo for obriga a percorrer a lista toda elemento a elemento 
# 4 -> O(m) - visto que o if neste caso vai comparar o elemento x a todos os elementos do dicionário , e caso não esteja no dicionário tem de percorre-lo todo
# 5 -> O(1) - porque o append a uma lista custa 1 
# 6 -> O(1) - pois o return do valor de uma variável custa 1 
# Assim a função tem complexidade O(n*m) sendo assim quadrática.



# CONFIRMAR A ALINEA 4


__author__ = "Rómulo Nogueira, 56935"


def busca_dicotomica(lista, elemento):
    """Função aprendida em aula que faz a busca de um elemento numa lista

    Requires:
        A lista estar ordenada
    Args:
        lista (list): Lista onde vai ser procurado o elemento 
        elemento (any): O elemento a procurar
    Returns:
        bool: True se o elemento está na lista; False caso contrário
    """
    def busca(primeiro, ultimo):
        if primeiro > ultimo:
            return False
        meio = (primeiro + ultimo) // 2
        if lista[meio] == elemento:
            return True
        if lista[meio] < elemento:
            return busca(meio + 1, ultimo)
        return busca(primeiro, meio - 1)
    return busca(0, len(lista) - 1)

def busca_lista_dupla(lista_dupla,elemento): 
    """Função que através da função auxiliar busca_dicotomica faz a busca de um elemento em listas duplas

    Requires:
        A lista dupla estar ordenada
        O elemento a procurar é um inteiro 
        nenhuma sublista é vazia 

    Args:
        lista_dupla (list): lista dupla na qual vai ser procurado o elemento 
        elemento (int): elemento a procurar na lista dupla

    Returns:
        bool: True caso o elemento esteja na lista dupla, False caso contrário
    """
    for sublista in lista_dupla:
        if busca_dicotomica(sublista,elemento) == True:
            return True 
    return False