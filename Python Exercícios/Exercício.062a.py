"""
[Exercício 62]
    Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.    

    [Exercício 61]
        Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura While.
    
        [Exercício 51]
            Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
    
"""

print('Calculadora de Progressão Aritmética.')
termo = int(input('Informe seu primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
contador = 0
resposta = 1

while resposta != 0:
    while contador < 10:
        print(termo, end=' -> ')
        termo = termo + razao
        contador += 1
    continuar = int(input('Mostrar mais quantos termos? '))
    if continuar >= 0:
        resposta = continuar
        while continuar > 0:
            print(termo, end=' -> ')
            termo = termo + razao
            continuar = continuar - 1     
    else:
        print('ERRO!')

print('Fim da progressão aritmética.')