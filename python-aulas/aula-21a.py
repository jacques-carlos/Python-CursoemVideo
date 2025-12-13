"""
**************************************************
AULA 21 parte a
**************************************************
        FUNÇÕES
        - Interactive Help 
        - Docstrings
        - Argumentos opcionais
        - Escopo de variáveis
        - Retorno de valores
"""
#INTERACTIVE HELP

#maneira 1
help(print)
#maneira 2
print(print.__doc__)

#DOCSTRINGS

def contador(i, f, p):
    """
    Docstring for contador
    
    -> Faz uma contagem e mostra na tela.

    :param i: início da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno
    
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    c = i
    while c <= f:
        print(c, end = ' ')
        c += p
    print('FIM!')

help(contador)

#PARÂMETROS OPCIONAIS
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma é {s}')
somar(1, 2, 3)
somar(4, 5)
somar(8)
somar()

#ESCOPO DE VARIÁVEIS - ESCOPO GLOBAL X ESCOPO LOCAL
def teste():
    x = 8 #variável local
    n = 5
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
n = 2 #variável global
print(f'Na função principal, n vale {n}')
teste()
#print(f'Na função principal, x vale {x}')

# global n -> utilizaria a variável global de n ao invés de criar uma variável local n

#RETORNO DE VALORES
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s
r1 = soma(3, 2, 5)
r2 = soma(1, 7)
r3 = soma(4)
print(f'As somas são: {r1} {r2} e {r3}')