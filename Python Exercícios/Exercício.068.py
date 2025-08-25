"""
[Exercício 65]
    Faça um programa que jogue par ou ímpar com o computadador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
    
"""

from random import randint
from time import sleep
contadorj = 1
contadorv = 0

while True:
    print('')
    print(f'******************** ROUND {contadorj} ********************')
    escolha = str(input('PAR ou ÍMPAR? ')).upper().strip()[0]
    if escolha not in 'PIÍ':
        print('ERRO! Digite uma opção válida!')
        break
    computador = randint(0,10)
    jogador = int(input('Seus dedos: '))
    print(' ')
    print('1...'), sleep(0.3)
    print('2...'), sleep(0.3)
    print('3...'), sleep(0.3)
    print('VAMOS VIRAR!!!'), sleep(0.3)
    print(' ')
    print(f'COMPUTADOR: {computador} | JOGADOR: {jogador}')
    soma = computador + jogador
    print(f'RESULTADO: {soma}')
    if soma % 2 == 0:
        print('PAR!')
        if escolha == 'P':
            print('COMPUTADOR escolheu: ÍMPAR | JOGADOR escolheu: PAR')
            print('Você VENCEU!')
            contadorv += 1
            contadorj +=1
        elif escolha in 'IÍ':
            print('COMPUTADOR escolheu: PAR | JOGADOR escolheu: ÍMPAR')
            print('Você PERDEU!')
            break
    else:
        print('ÍMPAR!')
        if escolha == 'P':
            print('COMPUTADOR escolheu: ÍMPAR | JOGADOR escolheu: PAR')
            print('Você PERDEU!')
            break
        elif escolha in 'IÍ':
            print('COMPUTADOR escolheu: PAR | JOGADOR escolheu: ÍMPAR')
            print('Você VENCEU!')
            contadorv += 1
            contadorj +=1
print(f'Total de vitórias consecutivas: {contadorv}')