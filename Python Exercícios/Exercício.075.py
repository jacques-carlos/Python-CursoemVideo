"""
[Exercício 75]
    Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.
    
"""

print('')
print('=-'*50)
print('')

while True:
    n1 = int(input('[1/4] Digite um número entre 0 e 10: '))
    if 0 <= n1 < 11:
        r1 = n1 % 2
        break

while True:
    n2 = int(input('[2/4] Digite um número entre 0 e 10: '))
    if  0 <= n2 < 11:
        r2 = n2 % 2
        break

while True:
    n3 = int(input('[3/4] Digite um número entre 0 e 10: '))
    if 0 <= n3 < 11:
        r3 = n3 % 2
        break

while True:
    n4 = int(input('[4/4] Digite um número entre 0 e 10: '))
    if 0 <= n4 < 11:
        r4 = n4 % 2
        break

tupla = (n1, n2, n3, n4)

print('')
print('=-'*50)
print('')

print(tupla)

print(f'O número 9 apareceu {tupla.count(9)} vez(es)')

if tupla.count(3) > 0:
    print(f'O primeiro número 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O número 3 não apareceu')

print('Os números pares são:', end=' ')
if r1 == 0:
    print(n1, end=" ")
if r2 == 0:
    print(n2, end=" ")
if r3 == 0:
    print(n3, end=" ")
if r4 == 0:
    print(n4, end=" ")