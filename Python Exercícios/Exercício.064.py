"""
[Exercício 64]
    Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles.
    (Desconsiderando o flag).
    
"""

c = 0
x = 0
soma = 0

while x != 999:
    x = int(input('Digite um número inteiro para a soma: '))
    if x != 999:
        c += 1
        soma += x
    else:
        print('Soma finalizada...')
print(f'Você digitou um total de {c} números e a soma deles é {soma}')