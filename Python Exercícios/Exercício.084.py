"""
[Exercício 84]
    Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pesssoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.
"""
pessoa = list()
grupo = list()
peso = list()
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    grupo.append(pessoa[:])
    pessoa.clear()
    resposta = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Resposta inválida! Digite [S] para SIM e [N] para NÃO: ')).strip()[0]
    if resposta in 'Nn':
        break
print(f'Foram cadastradas {len(grupo)} pessoas.')
for p in grupo:
    peso.append(p[1])
peso.sort(reverse = True)
maior = peso[0]
peso.sort()
menor = peso[0]
print(f'Com {maior:0.1f}Kg, as pessoas mais pesadas são: ', end=' ')
for ma in grupo:
    if ma[1] == maior:
        print(f'[{ma[0]}]', end = ' ')
print(f'\nCom {menor:0.1f}Kg, as pessoas mais leves são: ', end = ' ')
for me in grupo:
    if me[1] == menor:
        print(f'[{me[0]}]', end = ' ')