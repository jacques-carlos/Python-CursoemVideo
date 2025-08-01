"""
[Exercício 62]
    Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.    

    [Exercício 61]
        Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da Progressão usando a estrutura While.
    
        [Exercício 51]
            Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa Progressão.

        Neste versão do exercício 62 decidi fazer uma pequena alteração: perguntar ao usuário se ele deseja acrescentar mais termos na PA, em seguida perguntar a quantidade de 
    termos e por fim mostrar a Progressão Aritmética inteira.
    
"""

print('Calculadora de Progressão Aritmética.')
primeirotermo = int(input('Informe seu primeiro termo da PA: '))
termo = primeirotermo
razao = int(input('Informe a razão da PA: '))
contador = 0

while contador < 10:
    print(primeirotermo, end=' -> ')
    primeirotermo = primeirotermo + razao
    contador += 1
print('Fim da Progressão Aritmética.')

contador = 0

continuar = str(input('Deseja que eu mostre mais alguns termos? [S/N] ')).upper().strip()
if continuar == 'N':
     print('Certo, volte sempre que desejar!')
elif continuar == 'S':
    quantidade = int(input('Quantos termos a mais você deseja ver? '))
    if quantidade > 0:
        while contador < quantidade+10:
            print(termo, end=' -> ')
            termo = termo + razao
            contador += 1
        print('Fim da Progressão Aritmética.')
    else:
        print('ERRO! Selecione uma quantidade válida.')
else:
    print('ERRO! Por favor, digite "S" para SIM e "N" para NÃO.')