"""
[Exercício 60]
    Faça um programa que leia um número qualquer e mostre o seu fatorial.
    WHILE
    
"""
print('Programa que mostra o fatorial de um número.')
n = int(input('Digite um número: '))    # número
c = n                                   # contador
f = 1                                   # fator de multiplicação
print(f'Calculando {n}! =', end=(' '))
while c > 0:   
    # a condição a seguir serve para filtrar os números 0 e 1, que não precisam dessa parte
    if n > 1:
        print(c, end=' ')
        print('x' if c > 1 else '=', end=(' '))
        f *= c
        c -= 1
    else:
        break
# a condição a seguir serve para filtrar números negativos
if n >= 0:
    print(f)
else:
    print('Número inválido.')