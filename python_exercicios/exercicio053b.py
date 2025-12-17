"""
[Exercício 53]
    Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

"""

frase = str(input('Digite a frase: ')).upper().strip()
frase = frase.split()
frase = ''.join(frase)
inverso = ''

for x in range (len(frase)-1, -1, -1):
    inverso += frase[x]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')