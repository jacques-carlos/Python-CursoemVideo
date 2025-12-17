"""
[Exercício 29]
    Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada km acima do limite.

"""

velocidade = float(input('qual a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade-80)*7
    print(f'MULTADO! limite de velocidade excedido! você recebeu uma multa de R${multa:.2f} reais!')

else:
    print('nenhuma multa detectada, dirija com segurança!')