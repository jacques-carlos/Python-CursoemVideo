"""
[Exercício 100]
    Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().

    A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
"""
from time import sleep
from random import randint
def sorteia(números):
    print('Sorteando 5 valores para a lista:', end = ' ')
    for cont in range (0, 5):
        número = randint(1,10)
        números.append(número)
        print(número, end = ' ', flush=True)
        sleep(0.5)
    print('PRONTO!')
    sleep(3)
def somaPar(números):
    somapar = 0
    for valor in números:
        if valor % 2 == 0:
            somapar += valor
    print(f'Somando os valores pares de {números}, temos {somapar}.') 
números = list()
sorteia(números)
somaPar(números)