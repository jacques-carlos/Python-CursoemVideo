"""
[Exercício 24]
    Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

"""

cidade = str(input('Digite o nome da cidade:')).lower().strip()

lista = cidade.split()

print(lista[0] == 'santo')