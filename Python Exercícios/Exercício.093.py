"""
[Exercício 93]
    Crie um programa que gerencie o aproveitamento de um jogador de futebol.
    O programa vai ler o nome do jogador e quantas partidas ele jogou.
    Depois vai ler a quantidade de gols feitos em cada partida.
    No final isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = dict()
partidas = list()
total = 0
jogador['nome'] = str(input('Nome: '))
quantidade = int(input('Quantas partidas jogou? '))
for partida in range (0, quantidade):
    partidas.append(int(input(f'Quantos gols na partida {partida}? ')))
jogador['gols'] = partidas[:]
for gols in partidas:
    total += gols
jogador['total'] = total
print('='*50)
print(jogador)
print('='*50)
for k,v in jogador.items():    
    print(f'O campo {k} tem o valor {v}.')
print('='*50)
print(f'O jogador {jogador['nome']} jogou {quantidade} partidas.')
for c, p in enumerate(partidas):
    print(f' => Na partida {c}, fez {p} gols.')
print(f'Foi um total de {total} gols.')
print('='*50)