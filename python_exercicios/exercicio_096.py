"""
[Exercício 96]
    Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terrreno retangular (largura e comprimento) e mostre a área do terreno.
"""
def área(largura, comprimento):
    área = largura * comprimento
    print(f'A área de um terreno {largura:0.1f}x{comprimento:0.1f} é de {área:0.1f}m².')

print(f'{'Controle de Terrenos':^50}')
print('='*50)
área(float(input('LARGURA (em m): ')), float(input('COMPRIMENTO (em m): ')))