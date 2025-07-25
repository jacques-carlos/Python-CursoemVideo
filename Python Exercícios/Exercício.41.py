"""
[Exercício 41]
    A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

    - Até 9 anos: MIRIM
    - Até 14 anos: INFANTIL
    - Até 19 anos: JUNIOR
    - Até 25 anos: SÊNIOR
    - Acima: MASTER

"""

from datetime import date

ano = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - ano

print('*'*100)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print(f'Sua idade é de {idade} anos')
print('Sua categoria é:')

if idade <= 9:
    print('[MIRIM]')
elif idade <= 14:
    print('[INFANTIL]')
elif idade <= 19:
    print('[JUNIOR]')
elif idade <= 25:
    print('[SÊNIOR]')
elif idade > 25:
    print('[MASTER]')

print('*'*100)