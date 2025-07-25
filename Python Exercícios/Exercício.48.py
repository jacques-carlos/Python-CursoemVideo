"""
[Exercício 48]
    Crie um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
intervalo de 1 até 500.

"""

acumulador =0
contador = 0

for r in range(1, 501, 2):
    if r % 3== 0:
        acumulador += r
        contador += 1

print(f'Soma: {acumulador}\nQuantidade de números: {contador}')