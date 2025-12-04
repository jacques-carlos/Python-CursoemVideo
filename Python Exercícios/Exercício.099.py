"""
[Exercício 99]
    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

    Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep
def maior(*números):
    tamanho = cont = m = 0
    print('=' * 100)
    print('Analisando os valores passados...')
    sleep(1)
    for valor in números:
        print(valor, end= ' ', flush=True)
        sleep(0.5)
        tamanho += 1
        cont += 1
        if cont == 1:
            m = valor
        else:
            if valor > m:
                m = valor
    print(f'Foram informados {tamanho} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {m}.')
    sleep(2)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()