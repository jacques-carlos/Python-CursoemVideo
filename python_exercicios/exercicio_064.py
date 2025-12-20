"""
[Exercício 64]
    Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles.
    (Desconsiderando o flag).
    
"""
c = x = soma = 0       # c = contador # x = código para sair

while x != 999:
    x = int(input('Digite [999] para sair do programa | Digite um número qualquer para somar >>>>>> '))
    if x != 999:
        c += 1
        soma += x
    else:
        print('Soma finalizada...')
print(f'Você digitou um total de {c} números e a soma deles é {soma}')