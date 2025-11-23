"""
[Exercício 86 maneira A]
    Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
    No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [[], [], []]
matriz[0].append(int(input('Digite um valor para a posição [0, 0]: ')))
matriz[0].append(int(input('Digite um valor para a posição [0, 1]: ')))
matriz[0].append(int(input('Digite um valor para a posição [0, 2]: ')))
matriz[1].append(int(input('Digite um valor para a posição [1, 0]: ')))
matriz[1].append(int(input('Digite um valor para a posição [1, 1]: ')))
matriz[1].append(int(input('Digite um valor para a posição [1, 2]: ')))
matriz[2].append(int(input('Digite um valor para a posição [2, 0]: ')))
matriz[2].append(int(input('Digite um valor para a posição [2, 1]: ')))
matriz[2].append(int(input('Digite um valor para a posição [2, 2]: ')))
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')