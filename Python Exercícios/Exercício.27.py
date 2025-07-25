"""
[Exercício 27]
    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente.

"""


nome = str(input('Digite seu nome completo: ')).strip()

nome = nome.split()

print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[len(nome)-1]}')