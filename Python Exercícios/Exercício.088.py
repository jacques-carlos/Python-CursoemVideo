"""
[Exercício 88]
    Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
    O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
jogo = []
jogos = []
quantidade = int(input('Quantos jogos você deseja que eu faça? '))
for etapa in range (0, quantidade):
    cont = 0 #existem 0 números nesse jogo
    while True:
        num = randint(1,60)
        if num not in jogo: #elimina repetições
            jogo.append(num)
            cont += 1
        if cont == 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()

for x in range(0, quantidade):
    print(f'Jogo {x+1}: {jogos[x]}')
    sleep(1)
print('Boa sorte e jogue com responsabilidade!'.upper())