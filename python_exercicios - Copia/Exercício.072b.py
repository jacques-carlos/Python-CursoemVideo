"""
[Exercício 72]
    Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

    Adicional: perguntar se o usuário gostaria de continuar
    
"""

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:

    while True:
        escolha = int(input('Digite um número entre 0 e 20: '))
        if 20 > escolha >= 0:
            break
        else:
            print(f'Número inválido.', end=' ')

    print(f'Você digitou o número {extenso[escolha].upper()}')

    while True:
        resposta = str(
            input('Gostaria de continuar [s/n]: ')).upper().strip()[0]
        if resposta in 'SN':
            break

    if resposta == 'N':
        break

print('Volte sempre!')
