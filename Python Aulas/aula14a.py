"""
**************************************************
AULA 14 parte A
**************************************************

        ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO
        ESTRUTURA DE REPETIÇÃO WHILE

        x = 1
        while x < 10:
            print x
            x += 1
        print('FIM')
       
"""

x = 1
while x < 10:
    print(x)
    x += 1
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')

y = 1
par = impar = 0

while y != 0:
    y = int(input('Digite um número: '))
    if y != 0:
        if y % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares. Totalizando {par + impar} números.')