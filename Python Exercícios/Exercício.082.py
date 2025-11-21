"""
[Exercício 81]
    Crie um programa que vai ler vários números e colocar em uma lista.

    Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.

    Ao final, mostre o conteúdo das três listas geradas.

"""

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar? [s/n]: ')).strip()[0]
    if resposta in 'Nn':
        break
listap = []
listai = []
for n in lista:
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
print(f'Lista completa: {lista}')
print(f'Lista com PARES: {listap}')
print(f'Lista com ÍMPARES: {listai}')