"""
[Exercício 87]
    Aprimore o desafio anterior, mostrando no final:

    A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.

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

print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')

# SOMA DOS VALORES PARES
somaA = 0 
for n in matriz:
    c=0
    while True:
        if n[c] % 2 == 0:
            somaA += n[c]
        c += 1
        if c > 2:
            break
print(f'A soma dos números PARES é {somaA}')

# SOMA DOS VALORES DA TERCEIRA COLUNA
somaB = (matriz[0][2] + matriz[1][2] + matriz[2][2])
print(f'A soma dos valores da terceira coluna é {somaB}')

# MAIOR VALOR DA SEGUNDA LINHA

segundalinha = [matriz[1][0], matriz [1][1], matriz[1][2]]
segundalinha.sort()
print(f'O maior valor da segunda linha é: {segundalinha[-1]}')