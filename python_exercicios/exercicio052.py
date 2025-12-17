"""
[Exercício 52]
    Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

"""

n = int(input('Digite um número inteiro: '))        # Número
c = 0                                               # Contador

for x in range(1, n+1):
    if n % x == 0:
        print('\033[1;36m', end=' ')
        c += 1
    else:
        print('\033[1;31m', end=' ')
        c += 0
    print(x, end=' ')

print(f'\n\033[0mO número {n} possui {c} divisores')

if c == 2:                                  # p = 2 significa que o número será primo, pois os seus únicos divisores são 1 e ele mesmo
    print('Seu número É PRIMO!')
else:
    print('Seu número NÃO É PRIMO!')