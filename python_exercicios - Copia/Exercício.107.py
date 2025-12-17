"""
[Exercício 107]
    Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().

    Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
from utilidadescev import moeda

valor = float(input('Digite o valor: R$'))
print(f'O dobro de R${valor} é R${moeda.dobro(valor)}')
print(f'A metade de R${valor} é R${moeda.metade(valor)}')
print(f'Um aumento de 10% no valor R${valor} resulta em R${moeda.aumentar(valor, 10)}')
print(f'Uma diminuição de 13% no valor R${valor} resulta em R${moeda.diminuir(valor, 13)}')