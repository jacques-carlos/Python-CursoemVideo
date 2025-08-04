"""
[Exercício 62]
    Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.    

    [Exercício 61]
        Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da Progressão usando a estrutura While.
    
        [Exercício 51]
            Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa Progressão.
    
"""
print('Calculadora de Progressão Aritmética.')
termo = int(input('Informe seu primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
contador = 0
mais = 1

while mais != 0:
    while contador < 10:
        print(termo, end=' -> ')
        termo += razao
        contador += 1
    print('PAUSA')
    continuar = int(input('Mostrar mais quantos termos? '))
    if continuar >= 0:
        mais = continuar
        while continuar > 0:
            print(termo, end=' -> ')
            termo += razao
            continuar -= 1
            contador += 1
    else:
        print('ERRO!')

print(f'Fim da Progressão Aritmética com {contador} termos.')