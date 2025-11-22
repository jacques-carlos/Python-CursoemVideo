"""
[Exercício 86]
    Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
    No final, mostre a matriz na tela, com a formatação correta.

"""

linhaA = []
linhaB = []
linhaC = []

linhaA.append(int(input('Digite um valor para a posição [0, 0]: ')))
linhaA.append(int(input('Digite um valor para a posição [0, 1]: ')))
linhaA.append(int(input('Digite um valor para a posição [0, 2]: ')))
linhaB.append(int(input('Digite um valor para a posição [1, 0]: ')))
linhaB.append(int(input('Digite um valor para a posição [1, 1]: ')))
linhaB.append(int(input('Digite um valor para a posição [1, 2]: ')))
linhaC.append(int(input('Digite um valor para a posição [2, 0]: ')))
linhaC.append(int(input('Digite um valor para a posição [2, 1]: ')))
linhaC.append(int(input('Digite um valor para a posição [2, 2]: ')))

matriz = [linhaA[:], linhaB[:], linhaC[:]]

print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')

