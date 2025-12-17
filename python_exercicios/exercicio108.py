"""
[Exercício 108]
    Adapte o código do DESAFIO 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
"""
from utilidadescev import moeda

valor = float(input('Digite o valor: R$'))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(valor, 13))}')