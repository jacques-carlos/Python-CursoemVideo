"""
[Exercício 105]
    Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)

    Adicione também as docstrings da função.
"""
def notas(*num, sit=False):
    """
    Docstring for notas

    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a 'situação'.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = dict()
    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['média'] = sum(num) / len(num)
    if sit:
        if dados['média'] < 6:
            situação = 'RUIM'
        elif dados['média'] >= 8:
            situação = 'BOA'
        else:
            situação = 'RAZOÁVEL'
        dados['situação'] = situação
    return dados
# Programa principal
resultado = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resultado)