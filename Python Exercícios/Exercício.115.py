"""
[Exercício 115]
    Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.

    O sitema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
from utilidadescev.interface import *
from utilidadescev.arquivo import *

arquivo = 'lista.txt'

if not procurarArquivo(arquivo):
    criarArquivo(arquivo)  

while True:
    option = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if option == 1:
        lerArquivo(arquivo)
    elif option == 2:
        adicionarNome(arquivo)
    elif option == 3:
        título('Saindo do Sistema...')
        break
    else:
        print('\033[31mErro! Selecione uma opção válida.\033[m')       
print(linha('=', 50))
print('Até logo!')
print(linha('=', 50))