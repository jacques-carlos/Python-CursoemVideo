"""
[Exercício 103]
    Faça um programa que tenha uma função ficha() que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
    O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
def ficha(nome = '<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
# Programa principal
nome = str(input('Nome do jogador: '))
gols = str(input('Quantos gols: '))
if nome.isalpha() == False and gols.isnumeric() == False:
    ficha()
elif nome.isalpha() == False:
    ficha(gols = gols)
elif gols.isnumeric() == False:
    ficha(nome = nome)
else:
    ficha(nome, gols)