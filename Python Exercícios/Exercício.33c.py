"""
[Exercício 33]
    Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

"""

n1 = int(input('Digite primeiro numero: ')) 
n2 = int(input('Digite segundo numero: '))
n3 = int(input('Digite terceiro numero: '))
print('O maior numero é', max(n1, n2, n3))
print('O menor numero é', min(n1, n2, n3))