"""
[Exercício 45]
    Crie um programa que faça o computador jogar Jokenpô com você.
    
"""

from random import randint
from time import sleep

print("*"*100)
print(' ')

voce = str(input('Digite seu nome: '))
print(' ')

print('[1] Pedra\n[2] Papel\n[3] Tesoura')
print(' ')

jogador = int(input('Escolha: '))

print(' ')
print("*"*100)
print(' ')
sleep(2)

maquina = randint(1,3)

# 1 = Pedra
# 2 = Papel
# 3 = Tesoura

if jogador == 1 and maquina == 1:
    print(f'{voce} escolheu: Pedra\nMáquina escolheu: Pedra\n[EMPATE]')
elif jogador == 1 and maquina == 2:
    print(f'{voce} escolheu: Pedra\nMáquina escolheu: Papel\n[MÁQUINA VENCEU]')
elif jogador == 1 and maquina == 3:
    print(f'{voce} escolheu: Pedra\nMáquina escolheu: Tesoura\n[{voce.upper()} VENCEU]')
elif jogador == 2 and maquina == 1:
    print(f'{voce} escolheu: Papel\nMáquina escolheu: Pedra\n[{voce.upper()} VENCEU]')
elif jogador == 2 and maquina == 2:
    print(f'{voce} escolheu: Papel\nMáquina escolheu: Papel\n[EMPATE]')
elif jogador == 2 and maquina == 3:
    print(f'{voce} escolheu: Papel\nMáquina escolheu: Tesoura\n[MÁQUINA VENCEU]')
elif jogador == 3 and maquina == 1:
    print(f'{voce} escolheu: Tesoura\nMáquina escolheu: Pedra\n[M]ÁQUINA VENCEU]')
elif jogador == 3 and maquina == 2:
    print(f'{voce} escolheu: Tesoura\nMáquina escolheu: Papel\n[{voce.upper()} VENCEU]')
elif jogador == 3 and maquina == 3:
    print(f'{voce} escolheu: Tesoura\nMáquina escolheu: Tesoura\n[EMPATE]')
else:
    print('JOGADA INVÁLIDA')

print(' ')
print("*"*100)