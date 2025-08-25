"""
[Exercício 69]
    Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

    A) Quantas pessoas tem mais de 18 anos.
    B) Quantos homens foram cadastrados.
    C) Quantas mulheres tem menos de 20 anos.
    
"""

maiores = homens = mulheres = idade = 0

while True:
    sexo = 'a informar'
    continuar = 'a informar'
    print('')
    print('-'*50)
    print('CADASTRO DE PESSOAS')
    print('-'*50)

    idade = int(input('IDADE: '))
    if idade > 18:
        maiores += 1
    
    while sexo not in 'MF':
        sexo = str(input('SEXO[M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            homens += 1
        if idade < 20 and sexo == 'F':
            mulheres += 1    
    
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Há {maiores} pessoa(s) com mais de 18 anos.')
print(f'Há {homens} homem(s) cadastrado(s).')
print(f'Há {mulheres} mulher(es) com menos de 20 anos.')