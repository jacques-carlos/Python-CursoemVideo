"""
[Exercício 16]
    Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

"""

from math import trunc as inteiro # a função trunc passa a ser reconhecida como "inteiro" no código

r = float(input('digite um número real qualquer: '))
i = inteiro(r)
#i = int(r)     (também funciona)

print(f'O número {r} tem a parte inteira {i}.')