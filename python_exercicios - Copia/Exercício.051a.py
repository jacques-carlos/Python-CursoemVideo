"""
[Exercício 51]
    Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.

"""

n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for x in range(0, 10):
    print(n1, end=' -> ')
    n1 += r
print('FIM')