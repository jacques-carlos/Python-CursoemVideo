"""
[Exercício 18]
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

"""

import math

a = float(input('Digite o valor do ângulo: '))
r = math.radians(a) # tranformar o valor do ângulo de graus para radianos.

s = math.sin(r) #seno
c = math.cos(r) #cosseno
t = math.tan(r) #tangente

print(f'Seno: {s:.2f}\nCosseno: {c:.2f}\nTangente: {t:.2f}')