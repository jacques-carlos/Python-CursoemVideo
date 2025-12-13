"""
[Exercício 40]
    Escreva um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

    - Média abaixo de 5,0: REPROVADO
    - Média entre 5,0 e 6,9: RECUPERAÇÃO
    - Média 7,0 ou superior: APROVADO

"""

nota1 = float(input('Informe sua PRIMEIRA nota: '))
nota2 = float(input('Informe sua SEGUNDA nota: '))
media = (nota1 + nota2) /2

print(f'Primeira nota: {nota1:0.1f}')
print(f'Segunda nota: {nota2:0.1f}')
print(f'Média final: {media:0.1f}')

if media < 5:
    print('Situação: REPROVADO')
elif media >= 7:
    print('Situação: APROVADO')
else:
    print('RECUPERAÇÃO')