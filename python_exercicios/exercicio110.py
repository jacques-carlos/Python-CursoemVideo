"""
[Exercício 110]
    Adicione ao módulo moeda.py, criado nos desafios anteriores, uma função chamada resumo() que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""
from utilidadescev import moeda

valor = float(input('Digite o valor: R$'))
moeda.resumo(valor, 20, 12)