"""
[Exercício 19]
    Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
    Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido.

"""

"""
    Módulo: random
    Método: choice          escolhe aleatoriamente um único elemento de uma lista
"""

from  random import choice

print('Digite a seguir o nome dos quatro alunos:')
aluno1 = input('Nome do aluno (1/4): ')
aluno2 = input('Nome do aluno (2/4): ')
aluno3 = input('Nome do aluno (3/4): ')
aluno4 = input('Nome do aluno (4/4): ')

alunos=[aluno1, aluno2, aluno3, aluno4] # para o python uma lista tem que ficar entre colchetes

sorteado = choice(alunos)
print(f'O aluno sorteado foi {sorteado}.')