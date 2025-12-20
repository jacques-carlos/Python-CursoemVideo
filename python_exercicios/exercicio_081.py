"""
[Exercício 81]
    Crie um programa que leia vários números e colocar em uma lista.

    Depois disso mostre:

    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.

"""

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar? [s/n]: ')).strip()[0]
    if resposta in 'Nn':
        break
print(f'{len(lista)} números foram digitados')
lista.sort(reverse = True)
print(f'A lista desses números em ordem decrescente é: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado, portanto está na lista')
else:
    print('O valor 5 não foi digitado, portanto não está na lista')