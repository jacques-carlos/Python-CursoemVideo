"""
[Exercício 25]
    Crie um programa que leia o nome da pessoa e diga se ela tem "SILVA" no nome.

"""

nome = str(input('Digite seu nome: ')).lower().strip()

print('silva' in nome.split())