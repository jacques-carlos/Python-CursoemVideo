"""
[Exercício 34]
    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
    Para salários superiores a R$1250,00, calcule um aumento de 10%.
    Para os inferiores ou iguais o aumento é de 15%.

"""

print('Reajuste de salários.')
salario = float(input('Digite seu salário: R$'))

if salario > 1250.00:
    novosalario = salario + 0.1*salario

else:
    novosalario = salario + 0.15*salario

print(f'Seu novo salário é: R${novosalario:.2f} reais.')