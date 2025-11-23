"""
[Exercício 91]
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
    Guarde esses resultados em um dicionário.
    No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
resultados = dict()
pos = 0
for cont in range(1,5):
    resultados[f'Jogador{cont}'] = randint(1,6)
    print(f' O Jogador{cont} tirou {resultados[f'Jogador{cont}']}')
print('='*30)
print('Ranking dos jogadores:')
print('='*30)

for jogador, valor in resultados.items():
    pos += 1
    print(f'{pos}º lugar: {jogador} com {valor}')