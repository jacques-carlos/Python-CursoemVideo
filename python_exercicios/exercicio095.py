"""
[Exercício 95]
    Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
"""
lista = list()
jogador = dict()
partidas = list()
while True:
    total = 0
    jogador['nome'] = str(input('Nome: '))
    quantidade = int(input('Quantas partidas jogou? '))
    for p in range (0, quantidade):
        partidas.append(int(input(f'Quantos gols na partida {p}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    lista.append(jogador.copy())
    jogador.clear()
    partidas.clear()
    resposta = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Tente novamente. Deseja continuar? [S/N]: ')).strip()[0]
    if resposta in 'Nn':
        break

print('='*60)
print(f'{'cod.':<5}{'nome':<20}{'gols':<15}{'total':>5}')
for c, j in enumerate(lista):
    print(f'{c:<5}', end='')
    for info in j.values():
        print(f'{str(info):<20}', end = '')
    print('')
print('='*60)

while True:
    x = int(input('Mostrar dados de qual jogador? '))
    if x == 999:
        print('Encerrando o programa...')
        break
    if x not in range (0, len(lista)):
            print('Erro! Tente novamente.')
    else:    
        print(f'O jogador {lista[x]['nome']} jogou {len(lista[x]['gols'])} partidas.')
        for c, p in enumerate(lista[x]['gols']):
            print(f'        => Na partida {c}, fez {p} gols.')
        print(f'Foi um total de {lista[x]['total']} gols.')
        print('='*60)
print('='*60)
print('<< VOLTE SEMPRE >>')