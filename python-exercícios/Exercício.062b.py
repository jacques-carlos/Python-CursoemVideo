"""
[Exercício 62]
    Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.    

    [Exercício 61]
        Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da Progressão usando a estrutura While.
    
        [Exercício 51]
            Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa Progressão.

        Neste versão do exercício 62 decidi fazer uma pequena alteração: perguntar ao usuário se ele deseja acrescentar mais termos na PA e, em seguida, perguntar a quantidade de termos.

"""
print('Calculadora de Progressão Aritmética.')
termo = int(input('Informe seu primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
contador = 0
total = 0
quantidade = 10
continuar = 'S'
total += quantidade

while continuar != 'N':
    while contador < total:
        print(termo, end=' -> ')
        termo += razao
        contador += 1
    print('...')
    continuar = str(input('Deseja que eu mostre mais alguns termos? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
            print('Certo, volte sempre que desejar!')
    elif continuar == 'S':
        quantidade = int(input('Quantos termos a mais você deseja ver? '))
        total += quantidade
    else:
            print('ERRO! Por favor, digite "S" para SIM e "N" para NÃO.')
print(f'Calculadora de Progressão Aritmética encerrada com {total} termos.')