"""
[Exercício 76]
    Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.

    No final, mostre uma listagem de preços, organizando os dados em forma tabular.

"""

tupla = ('Caderno', 24.90, 'Lápis', 0.99, 'Caneta', 1.99, 'Borracha', 2.49, 'Pasta', 4.99, 'Mochila', 199.90, 'Estojo', 19.90)

print('-'*50)
print(f'{'LISTAGEM DE PREÇOS':^50}')
print('-'*50)

for p in range (0, len(tupla)):
    if p % 2 == 0:
        print(f'{tupla[p]:.<40}', end='')
    if p % 2 == 1:
        print(f'R${tupla[p]:7.2f}')