"""
[Exercício 107]
    Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().

    Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
import moeda

valor = float(input('Digite o valor: R$'))
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'Um aumento de 10% no valor {valor} resulta em {moeda.aumentar(valor, 10)}')
print(f'Uma diminuição de 13% no valor {valor} resulta em {moeda.diminuir(valor, 13)}')