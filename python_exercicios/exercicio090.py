"""
[Exercício 90]
    Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
    No final, mostre o conteúdo da estrutura na tela.
"""
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
while True:
    aluno['Média'] = float(input('Média: '))
    if 0 <= aluno['Média'] <=10:
        break
if aluno['Média']<7:
    aluno['Situação'] = 'reprovado'
else:
    aluno['Situação'] = 'aprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')