"""
[Exercício 57]
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""
sexo = str(input('Por favor, digite o seu sexo [M/F]: ')).upper().strip()[0]

while sexo not in 'MF':
    print('Opção inválida, tente novamente.')
    sexo = str(input('Por favor, digite o seu sexo [M/F]: ')).upper().strip()[0]
    
print(f'Sexo {sexo} registrado com sucesso')