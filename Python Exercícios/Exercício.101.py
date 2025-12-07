"""
[Exercício 101]
    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
"""
from datetime import date
def voto(idade):
    acesso = ''
    if idade < 16:
        acesso = 'NEGADO'
    elif idade >= 18 and idade < 65:
        acesso = 'OBRIGATÓRIO'
    else:
        acesso = 'OPCIONAL'
    return(acesso)
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print(f'Com {idade} anos: VOTO {voto(idade)}')