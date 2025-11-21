"""
[Exercício 80]
    Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
    No final, mostre a lista ordenada na tela
"""

lista = []

cont = pos = 0

for cont in range(0, 5):
    pos = 0
    numero = (int(input('Digite um valor: ')))

    if cont == 0:
        lista.insert(0, numero)
        print(f'Primeiro valor adicionado na lista...')
    else:
        while True:
            if pos == len(lista):
                lista.append(numero)
                print('Valor adicionado na posição final da lista...')
                break
            else:
                if numero < lista[pos]:
                    lista.insert(pos, numero)
                    print(f'Valor adicionado na posição {pos} da lista...')
                    break
                else:
                    pos += 1

print('=-'*30)
print('Os valores digitados em ordem foram:')
print(lista)
