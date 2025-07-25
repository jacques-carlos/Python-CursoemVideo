"""
[Exercício 35]
    Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
triângulo.

"""

retaA = float(input('Digite o valor da primeira reta: '))
retaB = float(input('Digite o valor da segunda reta: '))
retaC = float(input('Digite o valor da terceira reta: '))

if retaA + retaB > retaC and retaA + retaC > retaB and retaB + retaC > retaA:
    print('Suas retas podem formar um triângulo.')

else:
    print('Suas retas não podem formar um triângulo.')