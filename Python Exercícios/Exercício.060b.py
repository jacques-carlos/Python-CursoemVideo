"""
[Exercício 60]
    Faça um programa que leia um número qualquer e mostre o seu fatorial.
    FOR
    
"""

print('Programa que mostra o fatorial de um número.')
numero = int(input('Digite um número: '))
antecessor = numero - 1
resultado = numero * antecessor
for x in range (2, numero):
    antecessor = antecessor - 1
    resultado = resultado * antecessor
print(f'O resultado de {numero}! é: {resultado}')