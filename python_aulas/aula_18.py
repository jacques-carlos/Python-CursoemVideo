"""
**************************************************
AULA 18 - listas
**************************************************
        LISTAS
        Parte 2
"""

dadosP = list()
dadosP.append('Pedro')
dadosP.append(25)

dadosM = list()
dadosM.append('Maria')
dadosM.append(19)

dadosJ = list()
dadosJ.append('João')
dadosJ.append(32)

pessoas = list()
pessoas.append(dadosP[:])
pessoas.append(dadosM[:])
pessoas.append(dadosJ[:])

# ou

galera = [['Pedro', 25], ['Maria', 19], ['João', 32], ['Ana', 45]]

print(galera[0][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

dados = list()
pessoal = list()

# Input

maiores = menores = 0

for c in range(0, 3):
    pessoal.append(str(input('Digite o nome: ')))
    pessoal.append(int(input('Digite a idade: ')))
    dados.append(pessoal[:])
    pessoal.clear()
print(dados)
for x in dados:
    if x[1] >= 21:
        print(f'{x[0]} é maior de idade com {x[1]} anos')
        maiores += 1
    else:
        print(f'{x[0]} é menor de idade com {x[1]} anos')
        menores += 1
print(f'Há {maiores} maiores de idade e {menores} menores de idade')
