"""
[Exercício 57]
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""

sexo = ''
print('Seu sexo é masculino ou feminino?')

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida, tente novamente.')

if sexo == 'M':
    print('Seu sexo é masculino.')
elif sexo == 'F':
    print('Seu sexo é feminino.')