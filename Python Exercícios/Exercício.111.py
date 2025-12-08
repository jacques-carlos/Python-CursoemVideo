"""
[Exercício 111]
    Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
    Transfira todas as funções utilizadas nos DESAFIOS 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.
"""
from utilidadesCeV import moeda

valor = float(input('Digite o valor: R$'))
moeda.resumo(valor, 80, 35)

# Esse exercício ficou indêntico ao anterior, mas na verdade o Ex110 que foi alterado para continuar funcionando:
# import moeda -> from utilidadesCeV import moeda
