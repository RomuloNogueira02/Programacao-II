cidades = {'Lisboa': (38.7452, -9.1604), 
           'Vila Nova de Gaia': (41.1333, -8.6167),
           'Porto': (41.1495, -8.6108),
           'Braga': (41.5333, -8.4167),
           'Matosinhos': (41.2077, -8.6674),
           'Amadora': (38.75, -9.2333),
           'Almada': (38.6803, -9.1583),
           'Oeiras': (38.697, -9.3017),
           'Gondomar': (41.15, -8.5333),
           'Guimarães': (41.445, -8.2908),
           'Odivelas': (38.8, -9.1833),
           'Coimbra': (40.2111, -8.4291),
           'Vila Franca de Xira': (38.95, -8.9833),
           'Maia': (41.2333, -8.6167),
           'Leiria': (39.7431, -8.8069),
           'Setúbal': (38.5243, -8.8926),
           'Viseu': (40.6667, -7.9167),
           'Valongo': (41.1833, -8.5),
           'Viana do Castelo': (41.7, -8.8333),
           'Paredes': (41.2, -8.3333),
           'Vila do Conde': (41.35, -8.75),
           'Torres Vedras': (39.0833, -9.2667),
           'Barreiro': (38.6609, -9.0733),
           'Aveiro': (40.6389, -8.6553),
           'Queluz': (38.7566, -9.2545),
           'Mafra': (38.9333, -9.3333),
           'Penafiel': (41.2, -8.2833),
           'Loulé': (37.144, -8.0235)}

__author__ = "Rómulo Nogueira, 56935"

import operator
import math
import itertools
import functools

def distancia_itinerario(itinerario):
    """Função que calcula a distânica total de um itinerário

    Requires:
        Um itinerário tem de ter pelo menos duas cidades
        Itinerário com cidades válidas

    Args:
        itinerario (list): Lista com o itinerário

    Returns:
        float: Distância total do itinerário

    >>> round(distancia_itinerario(['Oeiras' , 'Oeiras']),3)
    0.0
    >>> round(distancia_itinerario(['Lisboa','Oeiras' , 'Oeiras']),3)
    13.166
    >>> round(distancia_itinerario(['Oeiras' , 'Queluz' , 'Queluz' , 'Lisboa' ]),3)
    15.858
    >>> round(distancia_itinerario(['Oeiras' , 'Almada' , 'Oeiras']),3)
    24.691
    >>> round(distancia_itinerario(['Porto' , 'Paredes', 'Coimbra' , 'Porto']),3)
    240.024
    >>> round(distancia_itinerario(['Loulé' , 'Lisboa']),3)
    202.64
    >>> round(distancia_itinerario(['Mafra' , 'Penafiel' , 'Guimarães']),3)
    294.67
    >>> round(distancia_itinerario(['Porto' , 'Aveiro' , 'Viseu', 'Lisboa' , 'Almada']),3)
    365.503
    """
    cidade_coordenada = list(map(lambda x: (x,cidades[x]), itinerario))
    coordenadas = list(map(operator.itemgetter(1), cidade_coordenada))
    coordenadas_convertidas = list(map(lambda x: (x[0]*111.1949, x[1]*85.1102) , coordenadas))
    resultado = sum(list(map(lambda x,y: math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2), coordenadas_convertidas[:-1], coordenadas_convertidas[1:])))
    return resultado

# Caracteristicas --> Blocos:
# nº de elementos do itinerário (n.e.i) --> 2, 3, >3
# Tem elementos repetidos? (e.r) --> True, False
# Os elementos repetidos estão seguidos? (e.r.s) --> True, False

#    Características e blocos      |                                Testes
#   n.e.i   |    e.r    |   e.r.s  |     input                                          |          resultado
#-----------|-----------|----------|----------------------------------------------------|----------------------------
#     2     |     T     |     T    | ['Oeiras' , 'Oeiras']                                          0.0
#     3     |     T     |     T    | ['Lisboa','Oeiras' , 'Oeiras']                                13.166
#    >3     |     T     |     T    | ['Oeiras' , 'Queluz' , 'Queluz' , 'Lisboa' ]            
#     2     |     T     |     F    |                                                INVIÁVEL                               
#     3     |     T     |     F    | ['Oeiras' , 'Almada' , 'Oeiras']                              15.858
#    >3     |     T     |     F    | ['Porto' , 'Paredes', 'Coimbra' , 'Porto']                    240.024
#     2     |     F     |     T    |                                                INVIÁVEL        
#     3     |     F     |     T    |                                                INVIÁVEL        
#    >3     |     F     |     T    |                                                INVIÁVEL        
#     2     |     F     |     F    | ['Loulé' , 'Lisboa']                                          202.64
#     3     |     F     |     F    | ['Mafra' , 'Penafiel' , 'Guimarães']                          294.67
#    >3     |     F     |     F    | ['Porto' , 'Aveiro' , 'Viseu', 'Lisboa' , 'Almada']           365.503                




##################################################################################################################################################################################
def adicionar_cidade(itinerario,cidade):
    """Função que adiciona uma cidade a um itinerário já existente

    Requires:
        O itinerário tem de ter pelo menos duas cidades
        A cidade tem de ser válida (estar no dicionário)

    Args:
        itinerario (list): Itinerário que vai ser adicionado a cidade
        cidade (str): Cidade que vai ser adicionada ao itinerário

    Returns:
        list: Lista com um novo itinerário que inclui a cidade
    
    >>> adicionar_cidade(['Loulé' , 'Porto'] , 'Loulé')
    ['Loulé', 'Loulé', 'Porto']
    >>> adicionar_cidade(['Oeiras', 'Aveiro' , 'Porto'] , 'Porto')
    ['Oeiras', 'Aveiro', 'Porto', 'Porto']
    >>> adicionar_cidade(['Lisboa','Oeiras','Porto' , 'Braga'] , 'Lisboa')
    ['Lisboa', 'Lisboa', 'Oeiras', 'Porto', 'Braga']
    >>> adicionar_cidade(['Braga','Guimarães','Porto'] , 'Guimarães')
    ['Braga', 'Guimarães', 'Guimarães', 'Porto']
    >>> adicionar_cidade(['Braga','Porto','Paredes','Aveiro'] , 'Paredes')
    ['Braga', 'Porto', 'Paredes', 'Paredes', 'Aveiro']
    >>> adicionar_cidade(['Lisboa','Porto'] , 'Loulé')
    ['Lisboa', 'Loulé', 'Porto']
    >>> adicionar_cidade(['Loulé', 'Almada' , 'Oeiras'] , 'Valongo')
    ['Loulé', 'Valongo', 'Almada', 'Oeiras']
    >>> adicionar_cidade(['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Porto'], 'Aveiro')
    ['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Aveiro', 'Porto']
    """
    novo_itinerario = list(itertools.islice(itinerario, 1, len(itinerario)-1))
    primeira, ultima = [itinerario[0]] , [itinerario[-1]]
    contador = list(itertools.takewhile(lambda x : x < (len(itinerario) - 1), itertools.count(0)))
    itinerario_provisorio = list(map(lambda count: novo_itinerario[:count] + [cidade] + novo_itinerario[count:] , contador))
    distancias = list(map(lambda it: distancia_itinerario(primeira + it + ultima) , itinerario_provisorio))
    minimo = distancias.index(min(distancias))
    novo_itinerario.insert(minimo,cidade)
    return primeira + novo_itinerario + ultima

# Caracteristicas --> Blocos:
# nº de elementos do itinerário original (n.e.i) --> 2, 3, >3
# A cidade a adicionar já está no itinerário? (c.i) --> True, False
# A cidade a adicionar é a igual à primeira ou à ultima do itinerário original? (c=p||c=u) --> True, False


#    Características e blocos      |                                        Testes
#   n.e.i   |    c.i    | c=p||c=u |     input                                                          |                               resultado
#-----------|-----------|----------|--------------------------------------------------------------------|-------------------------------------------------------------------
#     2     |     T     |     T    | (['Loulé', 'Porto'] , 'Loulé')                                        ['Loulé', 'Loulé', 'Porto']
#     3     |     T     |     T    | (['Oeiras', 'Aveiro' , 'Porto'] , 'Porto')
#    >3     |     T     |     T    | (['Lisboa', 'Oeiras', 'Porto', 'Braga'], 'Lisboa')                    ['Lisboa', 'Lisboa', 'Oeiras', 'Porto', 'Braga']
#     2     |     T     |     F    |                                                                 INVIÁVEL
#     3     |     T     |     F    | (['Braga','Guimarães','Porto'] , 'Guimarães')                         ['Braga', 'Guimarães', 'Guimarães', 'Porto']
#    >3     |     T     |     F    | (['Braga','Porto','Paredes','Aveiro'] , 'Paredes')                    ['Braga', 'Porto', 'Paredes', 'Paredes', 'Aveiro']
#     2     |     F     |     T    |                                                                 INVIÁVEL
#     3     |     F     |     T    |                                                                 INVIÁVEL
#    >3     |     F     |     T    |                                                                 INVIÁVEL
#     2     |     F     |     F    | (['Lisboa','Porto'] , 'Loulé')                                        ['Lisboa', 'Loulé', 'Porto']
#     3     |     F     |     F    | (['Loulé', 'Almada' , 'Oeiras'] , 'Valongo')                          ['Loulé', 'Valongo', 'Almada', 'Oeiras']
#    >3     |     F     |     F    | (['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Porto'], 'Aveiro')        ['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Aveiro', 'Porto']



##################################################################################################################################################################################
def construir_itinerario(origem, destino, lista_cidades):
    """Função que constrói um itinerário com base numa cidade de origem, 
        uma de destino e uma lista de cidades por onde passar
    
    Requires:
        origem , destino e lista_cidades contém cidades válidas

    Args:
        origem (str): Cidade de origem
        destino (str): Cidade de destino
        lista_cidades (list): Cidades por onde passar entre origem e destino 

    Returns:
        list: Itinerário completo 

    >>> construir_itinerario('Viseu', 'Viseu', ['Viseu'])
    ['Viseu', 'Viseu', 'Viseu']
    >>> construir_itinerario('Oeiras', 'Oeiras', ['Almada', 'Oeiras'])
    ['Oeiras', 'Oeiras', 'Almada', 'Oeiras']
    >>> construir_itinerario('Lisboa', 'Lisboa', ['Lisboa'])
    ['Lisboa', 'Lisboa', 'Lisboa']
    >>> construir_itinerario('Porto', 'Porto', ['Aveiro', 'Porto'])
    ['Porto', 'Porto', 'Aveiro', 'Porto']
    >>> construir_itinerario('Oeiras', 'Oeiras', [])
    ['Oeiras', 'Oeiras']
    >>> construir_itinerario('Lisboa', 'Lisboa', ['Setúbal'])
    ['Lisboa', 'Setúbal', 'Lisboa']
    >>> construir_itinerario('Loulé', 'Loulé', ['Gondomar', 'Barreiro', 'Almada'])
    ['Loulé', 'Gondomar', 'Almada', 'Barreiro', 'Loulé']
    >>> construir_itinerario('Lisboa', 'Porto', ['Lisboa'])
    ['Lisboa', 'Lisboa', 'Porto']
    >>> construir_itinerario('Oeiras', 'Loulé', ['Oeiras', 'Barreiro', 'Almada'])
    ['Oeiras', 'Oeiras', 'Almada', 'Barreiro', 'Loulé']
    >>> construir_itinerario('Lisboa', 'Braga', ['Braga'])
    ['Lisboa', 'Braga', 'Braga']
    >>> construir_itinerario('Braga', 'Loulé', ['Porto', 'Valongo', 'Loulé'])
    ['Braga', 'Valongo', 'Porto', 'Loulé', 'Loulé']
    >>> construir_itinerario('Lisboa', 'Porto', [])
    ['Lisboa', 'Porto']
    >>> construir_itinerario('Almada', 'Guimarães', ['Torres Vedras'])
    ['Almada', 'Torres Vedras', 'Guimarães']
    >>> construir_itinerario('Lisboa', 'Porto', ['Viseu', 'Coimbra', 'Setúbal', 'Aveiro'])
    ['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Aveiro', 'Porto']
    """
    itinerario = operator.concat([origem] , [destino])
    funcao_aux = lambda acc,cidade : adicionar_cidade(acc, cidade)
    itinerario = list(functools.reduce(funcao_aux, lista_cidades , itinerario))
    return itinerario

# Caracteristicas --> Blocos:
# Cidade de origem igual à de destino? (o = d) --> True, False
# tamanho da lista de cidades (t.l.c) --> 0, 1, >1
# Relação da lista_cidades com origem/destino (rel) --> lista_cidades contém cidade de origem (L C O)
#                                                   --> lista_cidades contém cidade de destino (L C D)
#                                                   --> nenhuma relação (nenhuma)


#    Características e blocos      |                        Testes
#   o = d   |   t.l.c   |    rel   |     input                                                      |                   resultado
#-----------|-----------|----------|----------------------------------------------------------------|-----------------------------------------------
#    T      |     0     |   L C O  |                                                            INVIÁVEL
#    T      |     1     |   L C O  | ('Viseu', 'Viseu', ['Viseu'])                                      ['Viseu', 'Viseu', 'Viseu']
#    T      |     >1    |   L C O  | ('Oeiras', 'Oeiras', ['Almada', 'Oeiras'])                         ['Oeiras', 'Oeiras', 'Almada', 'Oeiras']
#    T      |     0     |   L C D  |                                                            INVIÁVEL
#    T      |     1     |   L C D  | ('Lisboa', 'Lisboa', ['Lisboa'])                                   ['Lisboa', 'Lisboa', 'Lisboa']
#    T      |     >1    |   L C D  | ('Porto', 'Porto', ['Aveiro', 'Porto'])                            ['Porto', 'Porto', 'Aveiro', 'Porto']
#    T      |     0     |  nenhuma | ('Oeiras', 'Oeiras', [])                                           ['Oeiras', 'Oeiras']
#    T      |     1     |  nenhuma | ('Lisboa', 'Lisboa', ['Setúbal'])                                  ['Lisboa', 'Setúbal', 'Lisboa']
#    T      |     >1    |  nenhuma | ('Loulé', 'Loulé', ['Gondomar', 'Barreiro', 'Almada'])             ['Loulé', 'Gondomar', 'Almada', 'Barreiro', 'Loulé']
#    F      |     0     |   L C O  |                                                            INVIÁVEL
#    F      |     1     |   L C O  | ('Lisboa', 'Porto', ['Lisboa'])                                    ['Lisboa', 'Lisboa', 'Porto']       
#    F      |     >1    |   L C O  | ('Oeiras', 'Loulé', ['Oeiras', 'Barreiro', 'Almada'])              ['Oeiras', 'Oeiras', 'Almada', 'Barreiro', 'Loulé']
#    F      |     0     |   L C D  |                                                            INVIÁVEL
#    F      |     1     |   L C D  | ('Lisboa', 'Braga', ['Braga'])                                     ['Lisboa', 'Braga', 'Braga']
#    F      |     >1    |   L C D  | ('Braga', 'Loulé', ['Porto', 'Valongo', 'Loulé'])                  ['Braga', 'Valongo', 'Porto', 'Loulé', 'Loulé']
#    F      |     0     |  nenhuma | ('Lisboa', 'Porto', [])                                            ['Lisboa', 'Porto']
#    F      |     1     |  nenhuma | ('Almada', 'Guimarães', ['Torres Vedras'])                         ['Almada', 'Torres Vedras', 'Guimarães']
#    F      |     >1    |  nenhuma | ('Lisboa', 'Porto', ['Viseu', 'Coimbra', 'Setúbal', 'Aveiro'])     ['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Aveiro', 'Porto']



if __name__=="__main__":
    import doctest
    doctest.testmod()