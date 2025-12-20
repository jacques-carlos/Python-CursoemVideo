"""
**************************************************
AULA 8 parte B - biblioteca random
**************************************************

    random                                                                      módulo para operações randômicas
    randint                                                                     função que gera um número inteiro aleatório
    ao importar o módulo completo é necessário especificar módulo+função        ex: random.randint
    ao importar apenas a função basta informar função                           ex: sqrt
"""

import random

numero = random.randint(1, 10)
print(numero)

print(random.randint(1, 10))  # outra forma de fazer
