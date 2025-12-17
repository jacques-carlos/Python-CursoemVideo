"""
[Exercício 50]
    Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.

"""
soma=0
print('='*130)
print('Somador de números inteiros PARES\nNúmeros ÍMPARES não serão somados\nInforme 5 números inteiros QUAISQUER: ')
for r in range(1,6):
    n = int(input(f'Digite um número inteiro [{r}/5]: '))
    if n % 2 == 0:
        print(f'Esse número é PAR')
        soma += n
    else:
        print(f'Esse número é ÍMPAR')
        soma += 0
print(f'SUA SOMA É: {soma}')
print('='*130)