"""
[Exercício 94]
    Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
    No final mostre:
    A) Quantas pessoas foram cadastradas.
    B) A média de idade do grupo.
    C) Uma lista com todas as mulheres.
    D) Uma lista com todas as pessoas com idade acima da média.
"""
dados = list()
mulheres = list()
velhos = list()
somaidade = 0
while True:
    nome = str(input('Nome: ')).strip().title()
    sexo = str(input('Sexo [M/F]: ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Tente novamente. Sexo [M/F]: '))
    idade = int(input('Idade: '))
    somaidade += idade
    pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}
    dados.append(pessoa.copy())
    pessoa.clear()
    resposta = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Tente novamente. Deseja continuar? [S/N]: ')).strip()[0]
    if resposta in 'Nn':
        break
quantidade = len(dados)
média = somaidade/quantidade
print('='*50)
print(f' - Ao todo {quantidade} pessoas foram cadastradas.')
print(f' - A média de idade do grupo é de {média:0.1f} anos.')
for p in dados:
    if p['sexo'] == 'F':
        mulheres.append(p['nome'])
print(f' - As mulheres cadastradas foram: {mulheres}')
for v in dados:
    if v['idade'] > média:
        velhos.append(v['nome'])
print(f' - As pessoas com idade acima da média foram: {velhos}')