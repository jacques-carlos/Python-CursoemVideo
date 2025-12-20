"""
[Exercício 53]
    Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

"""

frase = str(input('Digite a frase: ')).upper().strip().replace(' ','')
caracteres = len(frase)
c = 0

for x in range(0, caracteres):
    if frase[x] == frase[caracteres-1-x]:
        c += 1

if c == caracteres:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')