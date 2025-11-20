"""
[Exercício 75]
    Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.
    
"""

while True:
    n1 = int(input('Digite um número entre 0 e 10: '))
    if 0 >= n1 < 11:
        if n1 % 2 == 0:
            p1 = n1
        break

while True:
    n2 = int(input('Digite outro número entre 0 e 10: '))
    if 0 >= n2 < 11:
        if n2 % 2 == 0:
            p2 = n2
        break

while True:
    n3 = int(input('Digite mais outro número entre 0 e 10: '))
    if 0 >= n3 < 11:
        if n3 % 2 == 0:
            p3 = n3
        break

while True:
    n4 = int(input('Digite um último número entre 0 e 10: '))
    if 0 >= n4 < 11:
        if n4 % 2 == 0:
            p4 = n4
        break

tupla = (n1, n2, n3, n4)
pares = ()

print(f'O número 9 apareceu {tupla.count('9')} vezes.')
print(f'O primeiro número 3 apareceu na {tupla.index('3')}ª posição.')
