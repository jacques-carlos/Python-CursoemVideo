"""
[Exercício 4]
    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
sobre ele.

"""

x=input('Digite um valor: ')

a=(type(x))
b=(x.isalnum())
c=(x.isnumeric())
d=(x.isalpha())
e=(x.isspace())
f=(x.isupper())
g=(x.islower())
h=(x.istitle())

print(f'A classe do valor é {a}')

print(f'É alfanumérico? {b}')
print(f'É numérico? {c}')
print(f'É alfabético? {d}')
print(f'É formados apenas por espaços? {e}')
print(f'Está em caixa-alta? {f}')
print(f'Está em caixa-baixa? {g}')
print(f'Está capitalizada? {h}')