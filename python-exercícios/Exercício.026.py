"""
[Exercício 26]
    Faça um programa que leia uma frase pelo teclado e mostre:

    1: Quantas vezes aparece a letra "A".
    2: Em que posição ela aparece a primeira vez.
    3: Em que posição ela aparece a última vez.

    *UNIDECODE: é um padrão que permite aos computadores representar e manipular texto de qualquer sistema de escrita
    existente utilizando códigos para caracteres individuais.

"""

from unidecode import unidecode

frase = str(input('Digite uma frase: ')).strip().lower()
frase = unidecode(frase)

#1
print(f'A letra "A" aparece {frase.count('a')} vezes na frase.')

#2
print(f'A primeira letra "A" apareceu na posição: {frase.find('a')+1}')

#3
print(f'A última letra "A" apareceu na posição: {frase.rfind('a')+1}')