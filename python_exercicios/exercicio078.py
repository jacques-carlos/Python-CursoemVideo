"""
[Exercício 78]
    Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

    No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

"""

lista = []
for valor in range (1,6):
    lista.append(int(input(f'[{valor}/5] Digite um valor : ')))

print('=-'*30)

print(f'Você digitou os valores: {lista}')

max = max(lista)
min = min(lista)

print('=-'*30)

print(f'O maior valor digitado foi {max} nas posições:', end=' ')
for i, n in enumerate(lista):
    if n == max:
        print(f'{i+1}...', end=' ')

print(f'\nO menor valor digitado foi {min} nas posições:', end=' ')    
for i, n in enumerate(lista):   
    if n == min:
        print(f'{i+1}...', end=' ')