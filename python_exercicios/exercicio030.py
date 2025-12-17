"""
[Exercício 30]
    Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

"""

numero = int(input('digite um número: '))
resto = numero % 2
print(f'o número escolhido foi:{numero}')

if resto == 0:
    print('seu número é par.')
else:
    print('seu número é ímpar.')