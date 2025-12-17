"""
[Exercício 15]
    Escreva um programa que pergunte a quantidade de km pecorridos por um carro alugado e quantidade de dias pelos
quais ele foi alugado.
    Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

"""

print('')
print('*'*28)
print(' JUBILEU LOCADORA DE CARROS')
print('*'*28)
print('')

carro = input('Informe o modelo do veículo: ')
placa = input('Informe a placa do veículo: ')
dias = int(input('Informe quantos dias de aluguel: '))
km = float(input('Informe quantos quilômetros rodados: '))
print('*'*100)

valor = dias * 60 + km * 0.15

print('')
print(f'Carro: {carro} \nPlaca: {placa}')
print(f'Total a pagar: R${valor:.2f}')