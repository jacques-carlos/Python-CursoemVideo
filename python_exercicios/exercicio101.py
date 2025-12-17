"""
[Exercício 101]
    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
"""
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'
ano = int(input('Ano de nascimento: '))
print(voto(ano))