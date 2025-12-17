"""
[Exercício 22]
    Crie um programa que leia o nome completo de uma pessoa e mostre:

    1: O nome com todas as letras maiúsculas.
    2: O nome com todas as letras minúsculas.
    3: Quantas letras no total (sem considerar espaços).
    4: Quantas letras tem o primeiro nome.

"""

nome = str(input('Insira seu nome completo: ')).strip()

#1
print(nome.upper())

#2
print(nome.lower())

#3
print('o total de letras é:',len(nome)-nome.count(' '))

#4
lista = nome.split()
print(f'O total de letras no primeiro nome é: {len(lista[0])}')