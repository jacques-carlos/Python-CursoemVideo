"""
**************************************************
AULA 8 parte A - biblioteca math; módulo sqrt
**************************************************

        ctrl + espaço                                       exibir opções
        python.org > docs > version > libre reference       informações
        python.org > PyPI                                   baixar pacotes
        settings > project > python interpreter             baixar pacotes
        from MÓDULO import FUNÇÃO ou import MÓDULO          importar módulos e funções
        math                                                módulo para funções matemáticas
        sqrt                                                função que calcula raiz quadrada
"""

from math import sqrt

numero = int(input('digite um número inteiro: '))

raiz = sqrt(numero)

print(f'a raiz de {numero} é igual a {raiz:.2f}')
