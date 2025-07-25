"""
[Exercício 14]
    Escreva um programa que converta uma temperatura digitada em ºC para ºF.
"""

celsius = float(input('Digite a temperatura em ºC: '))
fahrenheit = celsius * 1.8 + 32
print(f'{celsius}ºC equivale a {fahrenheit:.1f}ºF.')