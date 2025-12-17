"""
[Exercício 91]
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
    Guarde esses resultados em um dicionário.
    No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter
resultados = dict()
ranking = list()
pos = 0
for cont in range(1,5):
    resultados[f'Jogador{cont}'] = randint(1,6)
    print(f' O Jogador{cont} tirou {resultados[f'Jogador{cont}']} no dado.')
    sleep(1)
print('='*30)
print(f'{'Ranking dos jogadores:':^30}'.upper())
print('='*30)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
for jogador, valor in ranking:
    pos += 1
    print(f'{pos}º lugar: {jogador} com {valor}.')
    sleep(1)