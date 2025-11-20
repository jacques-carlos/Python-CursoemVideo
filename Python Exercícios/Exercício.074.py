"""
[Exercício 74]
    Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
    Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
    
"""

from random import randint

n1 = randint(0, 1000)
n2 = randint(0, 1000)
n3 = randint(0, 1000)
n4 = randint(0, 1000)
n5 = randint(0, 1000)

tupla = (n1, n2, n3, n4, n5)
print(f'A tupla criada foi: {tupla}')
print(f'O maior número é: {sorted(tupla)[-1]}')
print(f'O menor número é: {sorted(tupla)[0]}')