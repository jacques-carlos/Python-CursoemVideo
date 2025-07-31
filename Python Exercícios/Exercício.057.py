"""
[Exercício 57]
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""

sexo = 0

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()

if sexo == 'M':
    print('Seu sexo é masculino')
elif sexo == 'F':
    print('Seu sexo é feminino')