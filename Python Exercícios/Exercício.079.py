"""
[Exercício 79]
    Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
    Caso o número já exista lá dentro, ele não será adicionado.
    No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
"""

lista = list()

while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        print('Valor adicionado com sucesso...')
        lista.append(n)
    else:
        print('Valor duplicado! Não vou adicionar...')
   
    resposta = str(input('Deseja continuar? [s/n]: ')).strip()[0]
    if resposta in 'Nn':
        break

lista.sort()
print('=-'*30)
print(f'Os valores digitados foram: {lista}')