"""
[Exercício 10]
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
    Considere USD$1,00 = R$3,27
"""

d=float(input('Quanto dinheiro (em R$) você tem? R$'))

print(f'Com R${d:0.2f} você pode comprar USD${d/3.27:0.2f}')