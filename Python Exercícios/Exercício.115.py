"""
[Exercício 115]
    Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.

    O sitema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
from utilidadescev import geral

option = 0
while option != 3:
    geral.título('Menu principal')
    print('\033[1;34m1 -\033[m Ver pessoas cadastradas')
    print('\033[1;34m2 -\033[m Cadastrar nova pessoa')
    print('\033[1;34m3 -\033[m Sair do Sistema')
    geral.linha('=')
    while True:
        try:
            option = int(input('\033[1;34mSua opção: \033[m'))
        except:
            print('\033[31mErro! Digite um número válido.\033[m')
        else:
            if option == 1:
                geral.título('Opção 1')
                break
            if option == 2:
                geral.título('Opção 2')
                break
            if option == 3:
                geral.título('Saindo do Sistema...')
                break
            else:
                print('\033[31mErro! Selecione uma opção válida.\033[m')       
print('Até logo!')
geral.linha('=')