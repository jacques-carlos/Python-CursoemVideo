"""
[Exercício 71]
    Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

"""
valor = notas_cinquenta = notas_vinte = notas_dez = notas_um = 0

print('='*50)
print(f'{'BANCO MP':^50}')
print('='*50)

while True:
    valor = int(input('Quanto você deseja sacar? '))
    while valor >= 50:
        valor = valor - 50
        notas_cinquenta += 1
    while valor >= 20:
        valor = valor - 20
        notas_vinte += 1
    while valor >= 10:
        valor = valor - 10
        notas_dez +=1
    while valor >= 1:
        valor = valor - 1
        notas_um += 1
    break

print('='*50)

if notas_cinquenta > 0:
    if notas_cinquenta == 1:
        print(f'{notas_cinquenta} nota de R$50')
    else:
        print(f'{notas_cinquenta} notas de R$50')

if notas_vinte > 0:
    if notas_vinte == 1:
        print(f'{notas_vinte} nota de R$20')
    else:
        print(f'{notas_vinte} notas de R$20')

if notas_dez > 0:
    if notas_dez == 1:
        print(f'{notas_dez} nota de R$10')
    else:
        print(f'{notas_dez} notas de R$10')

if notas_um > 0:
    if notas_um == 1:
        print(f'{notas_um} nota de R$1')
    else:
        print(f'{notas_um} notas de R$1')
        
print('='*50)