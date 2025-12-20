"""
**************************************************
AULA 20 - funções
**************************************************
        FUNÇÕES
        - def
        - empacotar e desempacotar
"""


def lin():
    print('')
    print('=' * 100)
    print('')


lin()
# criando uma função para somar dois valores:


def soma(a, b):
    s = a + b
    print(s)


soma(a=4, b=5)
soma(8, 9)
soma(2, 1)
soma(4, 1)

lin()
# criando uma função de contador (EMPACOTAMENTO):


def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

lin()
# criando uma função para dobrar os valores de listas:


def dobro(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


lista = [7, 2, 5, 0, 4]
dobro(lista)
print(lista)

lin()
# criando uma função para somar vários valores (DESEMPACOTAMENTO):


def soma(*valores):
    total = 0
    for num in valores:
        total += num
    print(f'Somando os valores {valores} temos {total}.')


soma(6, 8)
soma(3, 1, 4)
soma(1, 9, 2, 5)

lin()
