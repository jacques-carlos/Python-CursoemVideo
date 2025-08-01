"""
[Exercício 58]
    Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

    [Exercício 28]
        Escreva um programa que faça o computador "pensar" em número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.   
        O programa deverá escrever na tela se o usuário venceu ou perdeu.    

"""
from random import randint

computador = randint(0,10)
usuario = 11
tentativas = 0
print('Você é bom em adivinhação?')

while computador != usuario:
    print('Estou pensando em um número entre 0 e 10... Tente adivinhar!')
    usuario = int(input('Digite seu palpite: '))
    if usuario > 10:
        print('Por favor, informe um número válido.')
    else:
        tentativas += 1
        if computador != usuario:
            print('Que pena, você errou!')
print(f'Parabéns, você acertou! Você precisou de {tentativas} tentativa(s).')