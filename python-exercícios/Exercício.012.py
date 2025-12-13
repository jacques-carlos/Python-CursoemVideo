"""
[Exercício 12]
    Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

"""

x=float(input('Digite o preço do produto aqui: R$'))

print(f'Preço atual do produto: R${x:0.2f}\nEm seu produto será aplicado 5% de desconto.\nSeu preço agora é de R${x-0.05*x:0.2f}')