"""
**************************************************
AULA 19 - dicionários
**************************************************
        DICIONÁRIO
        variáveis compostas mutáveis
        values() + keys() = items()
"""

dicionario = dict()

print('='*100)
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
dados['sexo'] = 'M'
del dados['idade']
print(dados)

print('='*100)
filme = {
    'Título': 'Star Wars',
    'Ano': 1977,
    'Diretor': 'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')

print('='*100)
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 92.5
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')

print('='*100)
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['nome'] = str(input('Digite o Estado: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())
for est in brasil:
    print('')
    for k, v in est.items():
        print(f'O campo {k} tem valor {v}.')
