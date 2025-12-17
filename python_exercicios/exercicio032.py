"""
[Exercício 32]
    Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

"""

from datetime import date

ano = int(input('Que ano quer analisar? Digite "0" para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

# Para um ano ser bissexto ele necessita ser divisível por 4 e não ser múltiplo de 100 (exceto seja múltiplo de 400).

# Se o ano for divisível por 4 e não for múltiplo de 100, ou for múltiplo de 400:
if ano%4==0 and ano%100!=0 or ano%400==0:
    print(f'O ano {ano} é bissexto.')

else:
    print(f'O ano {ano} não é bissexto.')