"""
[Exercício 58]
    Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

    [Exercício 28]
        Escreva um programa que faça o computador "pensar" em número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.   
        O programa deverá escrever na tela se o usuário venceu ou perdeu.    

"""
from random import randint
print('Você é bom em adivinhação?')
print('Estou pensando em um número entre 0 e 10... Tente adivinhar!')
computador = randint(0,10)
usuario = int(input('Digite seu palpite: '))
tentativas = 1

while computador != usuario:   
    if usuario > 10 or usuario <0:
        print('Por favor, informe um número válido.')
    else:
        if computador > usuario:
            dica = 'Mais...'
        elif computador < usuario:
            dica = 'Menos...'
        print(dica)
        tentativas += 1
    usuario = int(input('Tente outra vez: '))

print(f'Parabéns, acertou! Você precisou de {tentativas} tentativa(s).')