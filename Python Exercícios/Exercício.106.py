"""
[Exercício 106]
    Faça um mini-sistema que utilize o Interactive Help do Python.
    O usuário vai digitar o comando e o manual vai aparecer.
    Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

    OBS: use cores.
"""


def título(frase):
    print('\033[1;33;41m')
    print('='*len(frase))
    print(frase)
    print('='*len(frase))
    print('\033[m')


def PyHelp(nome):
    título(f'ACESSANDO O MANUAL DO COMANDO {nome.upper()}')

    print('\033[1;30;107m')
    help(nome)
    print('\033[m')


while True:
    título('SISTEMA DE AJUDA PyHelp')
    nome = str(input('Função ou Biblioteca: ')).lower()
    if nome == 'fim':
        break
    PyHelp(nome)

título('ATÉ LOGO!')