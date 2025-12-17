"""
[Exercício 17]
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.

"""

from math import sqrt as r, hypot as hip # é possível importar mais de uma função especificada

co = float(input('Valor do cateto oposto (em cm): '))
ca = float(input('Valor do cateto adjacente (em cm): '))
hi = hip(co, ca)
# hi = r(pow(co, 2) + pow(ca, 2))

print(f'O comprimento da hipotenusa é {hi:.2f}cm.')