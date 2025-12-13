"""
[Exercício 4]
    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
sobre ele.

"""

x=input('Digite qualquer informação: ')

print('O tipo primitivo (classe) dessa informação é:',type(x))

print('É alfanumérica?', x.isalnum())
print('É alfabética?', x.isalpha())
print('É numérica?', x.isnumeric())
print('É formada apenas por espaço(s)?', x.isspace())
print('Está em caixa-baixa?', x.islower())
print('Está em caixa-alta?', x.isupper())
print('Está capitalizada?', x.istitle())