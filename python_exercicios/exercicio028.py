"""
[Exercício 28]
    Escreva um programa que faça o computador "pensar" em número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
    O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""

from random import randint
" randint -> método para randomizar um número inteiro"

from time import sleep
" sleep -> método de tempo para representar um delay"


numero1 = randint(0,5)
numero2 = int(input('tente adivinha um número entre 0 e 5: '))

print('carregando...')
sleep(3)

if numero1 == numero2:
    print('você acertou!')
else:
    print('você errou!')

print(f'número escolhido: {numero2}\nnúmero sorteado: {numero1}')