"""
[Exercício 76]
    Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.

    No final, mostre uma listagem de preços, organizando os dados em forma tabular.

"""

x=0
tupla = ('Caderno', 24.90, 'Lápis', 0.99, 'Caneta', 1.99, 'Borracha', 2.49, 'Pasta', 4.99, 'Mochila', 199.90, 'Estojo', 19.90)

print('-'*70)
print(f'{'LISTAGEM DE PREÇOS':^70}')
print('-'*70)

print (tupla[0], end='')
print(f'{'R$':.>60}', end='')
print(f'{tupla[1]:0.2f}')

print (tupla[2], end='')
print(f'{'R$':.>60}', end='')
print(f'{tupla[3]:0.2f}')

print (tupla[4], end='')
print(f'{'R$':.>60}', end='')
print(f'{tupla[5]:0.2f}')

print (tupla[6], end='')
print(f'{'R$':.>60}', end='')
print(f'{tupla[7]:0.2f}')

print (tupla[8], end='')
print(f'{'R$':.>60}', end='')
print(f'{tupla[9]:0.2f}')

print (tupla[10], end='')
print(f'{'R$':.>60}', end='')
print(f'{tupla[11]:0.2f}')

print (tupla[12], end='')
print(f'{'R$':.>60)}', end='')
print(f'{tupla[13]:0.2f}')

print('-'*70)