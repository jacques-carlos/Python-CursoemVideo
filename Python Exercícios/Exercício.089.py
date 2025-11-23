"""
[Exercício 89]
    Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
    No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar notas de cada alunos individualmente.
"""
cont=0
boletim = []

while True:
    cont+=1
    aluno = []
    notas = []
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    aluno.append(notas[:])
    boletim.append(aluno[:])
    notas.clear()
    aluno.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Resposta inválida. Digite [S] para SIM e [N] para NÃO: ')).strip()[0]
    if continuar in 'Nn':
        break

while True:
    print('')
    print('='*60)
    print(f'{'Num.':<5}{'NOME':<15}{'MÉDIA':>5}')
    for num in range (0, cont):
        print('-'*25)
        print(f'{num:<5}{boletim[num][0]:<15}{(boletim[num][1][0]+boletim[num][1][1])/2:>5.1f}')
    print('='*60)
    while True:
        detalhe = int(input('\nMostrar notas de qual aluno? (999 interrompe): '))
        if detalhe == 999:
            break
        if detalhe in range (0, cont):
            print(f'As notas de {boletim[detalhe][0]} são {boletim[detalhe][1]}')
        else:
            print('Número inválido. Por favor, tente novamente')
    print('='*60)
    print('Finalizando...'.upper())
    break