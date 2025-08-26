"""
[Exercício 70]
    Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
        A) Qual é o total gasto na compra.
        B) Quantos produtos custam mais de R$1000.
        C) Qual o nome do produto mais barato.
    
"""
total = produtos_caros = preço_mais_barato = 0
nome_mais_barato = ''

print('-'*50)
print(f'{' LOJA MERCADO PRESO ':=^50}')
print('-'*50)

while True:
    continuar = 'a definir'
    print('')
    produto = (str(input('Produto: ')))
    preço = float(input('Preço: R$'))

    if total == 0 or preço < preço_mais_barato:
        nome_mais_barato = produto
        preço_mais_barato = preço

    total += preço
    
    if preço > 1000:
        produtos_caros += 1

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('')
print(f'Total gasto na compra: R${total:.2f}')
print(f'{produtos_caros} produtos custam mais de R$1000.')
print(f'O produto mais barato é: {nome_mais_barato}, que custou R${preço_mais_barato:.2f}')