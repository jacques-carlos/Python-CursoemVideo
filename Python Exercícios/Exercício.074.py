"""
[Exercício 74]
    Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
    Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
    
"""

from random import randint

tupla = (randint(1, 9), randint(1, 9), randint(
    1, 9), randint(1, 9), randint(1, 9))

print('Os valores sortados foram:', end=' ')
for n in tupla:
    print(n, end=' ')

# print(f'O maior número foi: {sorted(tupla)[-1]}')
# print(f'O menor número foi: {sorted(tupla)[0]}')

print(f'\nO maior número foi: {max(tupla)}')

print(f'O maior número foi: {min(tupla)}')
