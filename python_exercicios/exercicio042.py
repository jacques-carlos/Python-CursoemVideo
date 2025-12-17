"""
[Exercício 42]
    Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

    - Equilátero: todos os lados iguais
    - Isósceles: dois lados iguais
    - Escaleno: todos os lados diferentes

    [Exercício 35] Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
    formar um triângulo.

"""

x = 0

print('*'*50)

retaA = float(input('Digite o valor da primeira reta: '))
retaB = float(input('Digite o valor da segunda reta: '))
retaC = float(input('Digite o valor da terceira reta: '))

print('*'*50)

if retaA + retaB > retaC and retaA + retaC > retaB and retaB + retaC > retaA:
    print('Suas retas podem formar um Triângulo.')

    if retaA == retaB == retaC:
        print('Tipo do triângulo: Equilátero.')
    elif retaA != retaB != retaC != retaA:
        print('Tipo do triângulo: Escaleno.')
    else:
        print('Tipo do triângulo: Isósceles.')

else:
    print('Suas retas não podem formar um Triângulo.')