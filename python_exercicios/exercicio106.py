"""
[Exercício 106]
    Faça um mini-sistema que utilize o Interactive Help do Python.
    O usuário vai digitar o comando e o manual vai aparecer.
    Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

    OBS: use cores.
"""
from time import sleep

cores = ('\033[m',                  # 0 - sem cor
         '\033[0;30;41m',           # 1 - vermelho
         '\033[0;30;42m',           # 2 - verde
         '\033[0;30;43m',           # 3 - amarelo
         '\033[0;30;44m',           # 4 - azul
         '\033[0;30;45m',           # 5 - roxo
         '\033[0;30;107m'           # 6 - branco
        )

def título(mensagem, cor=0):
    tamanho = len(mensagem)+4
    print(cores[cor], end='')
    print('=' * tamanho)
    print(f'{mensagem:^{tamanho}}')
    print('=' * tamanho)
    print(cores[0], end='')
    sleep(1)

def ajuda(nome):
    print(f'ACESSANDO O MANUAL DO COMANDO {nome.upper()}',5)
    print(cores[6], end='')
    help(nome)
    print(cores[0], end='')
    sleep(1)

while True:
    título('SISTEMA DE AJUDA PYHELP', 4)
    comando = str(input('Função ou Biblioteca > '))
    if comando.lower() == 'fim':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)

# OBSERVAÇÃO DO ALUNO: não sei ainda exatamente o porquê, mas o Código ANSI, a função HELP e o VS CODE não dialogam entre si muito bem.