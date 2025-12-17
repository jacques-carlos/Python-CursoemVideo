"""
[Exercício 20]
    O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
    Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

"""

from random import shuffle # função que embaralha os elementos de uma lista

print('Digite a seguir o nome dos quatro alunos:')

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)