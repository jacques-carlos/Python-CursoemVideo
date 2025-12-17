"""
[Exercício 39]
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

    - Se ele ainda vai se alistar no serviço militar.
    - Se é hora de se alistar.
    - Se já passou do tempo do alistamento.

    O seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""

from datetime import date

nome = str(input('Informe seu nome: '))
ano = int(input('Informe o ano do seu nascimento: '))
idade = date.today().year - ano

if idade < 18:
    print(f'''
Nome: {nome}
Idade: {idade}
Ano de alistamento: {ano+18}
Ano atual: {date.today().year}
Situação: Deve se alistar no exército em {18-idade} ano(s)''')

elif idade == 18:
    print(f'''
Nome: {nome}
Idade: {idade}
Ano de alistamento: {ano+18}
Ano atual: {date.today().year}
Situação: Deve se alistar no exército neste exato ano''')

else:
    print(f'''
Nome: {nome}
Idade: {idade}
Ano de alistamento: {ano+18}
Ano atual: {date.today().year}
Situação: Deveria ter se alistado no exército há {idade-18} ano(s)''')