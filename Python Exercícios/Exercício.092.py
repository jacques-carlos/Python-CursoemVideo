"""
[Exercício 92]
    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
    Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
    Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
an = int(input('Ano de nascimento: ')) # an:ano de nascimento
pessoa['idade'] = date.today().year - an
pessoa['ctps'] = int(input('Carteira de trabalho: '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - an
for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')