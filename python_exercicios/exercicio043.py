"""
[Exercício 43]
    Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o seu status, de acordo
com a tabela abaixo:

    - Abaixo de 18.5: Abaixo do Peso
    - Entre 18.5 e 25: Peso ideal
    - 25 até 30: Sobrepeso
    - 30 até 40: Obesidade
    - Acima de 40: Obesidade mórbida

"""

print('*'*100)

massa = float(input('Informe sua massa (Kg): '))
altura = float(input('Informe sua altura (m): '))
imc = massa / altura**2

if imc < 18.5:
    status = 'ABAIXO DO PESO'
elif imc <= 25:
    status = 'PESO IDEAL'
elif imc <= 30:
    status = 'SOBREPESO'
elif imc <= 40:
    status = 'OBESIDADE'
else:
    status = 'OBESIDADE MÓRBIDA'

print(f'IMC: {imc:0.1f}')
print(f'Status: {status}')

print('*'*100)