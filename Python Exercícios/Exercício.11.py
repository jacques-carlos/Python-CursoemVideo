"""
[Exercício 11]
    Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

"""

print('Calcular área da parede:')

base=float(input('Informe a largura da parede (em metros): '))
altura=float(input('Informe a altura da parede (em metros): '))

a=base*altura

print(f'A área da parede é de {a:0.2f}m²\nÉ(são) necessário(s) {a/2:0.3f} litro(s) de tinta.')