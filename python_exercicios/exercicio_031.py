"""
[Exercício 31]
    Deselvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50
por km para viagens de até 200Km e R$0,45 para viagens mais longas.

"""

distancia = float(input('Informe a distância de sua viagem: '))

if distancia > 200:
    custo = distancia * 0.45

else:
    custo = distancia * 0.5

print(f'O preço da passagem de sua viagem de {distancia}km é R${custo:.2f} reais.')