"""
**************************************************
AULA 21 parte c
**************************************************
        PAR OU ÍMPAR
"""


def par(num):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('Esse número é par!')
else:
    print('Esse número é ímpar!')
