"""
[Exercício 54]
    Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.

"""

from datetime import date
hoje = date.today().year
maior = 0
menor = 0

for x in range(1,8):
    print(f'Pessoa [{x}/7]')
    nome = str(input('Digite o seu nome: '))
    ano = int(input(f'Olá, {nome}. Digite o seu ano de nascimento: '))
    idade = hoje - ano
    if idade <21:
        menor += 1
    else:
        maior += 1
print(f'{maior} pessoa(s) atingiram a maioridade.')
print(f'{menor} pessoa(s) ainda não atingiram a maioridade.')