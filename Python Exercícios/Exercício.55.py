"""
[Exercício 55]
    Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

"""

maior = 0
menor = 0
pessoa1 = ''
pessoa2 = ''

for y in range(1,6):
    print(f'Pessoa [{y}/5]')
    nome = str(input('Digite seu nome: ')).strip()
    peso = float(input(f'Olá, {nome}. Digite seu peso: '))
    if y == 1:
        maior = peso
        menor = peso
        pessoa1 = nome
        pessoa2 = nome
    else:
        if peso == maior:
            pessoa1 += ' e ' + nome
        elif peso > maior:
                maior = peso
                pessoa1 = nome
        if peso == menor:
            pessoa2 += ' e ' + nome
        elif peso < menor:
            menor = peso
            pessoa2 = nome

print(f'Maior peso: {pessoa1} com {maior:0.2f}Kg')
print(f'Menor peso: {pessoa2} com {menor:0.2f}Kg')