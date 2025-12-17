"""
[Exercício 36]
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
    Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
negado.

"""

casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salário mensal: R$'))
tempo = int(input('Informe em quantos anos você gostaria de quitar as prestações: '))
prestacao = casa/(tempo*12)
valormaximo = salario * 0.3

print(' ')
if prestacao > valormaximo:
    print('Caro senhor(a), infelizmente seu empréstimo foi negado devido a inviabilidade financeira de seu orçamento.')
    print('Por favor, solicite um tempo maior de prestações ou busque um salário maior.')

else:
    print(f'Empréstimo aprovado! As prestações ficarão em um valor de R${prestacao:0.2f} mensais durante {tempo} anos.')

print(' ')
print('*'*50)
print(f'Informações Gerais:')
print(f'Valor da casa: R${casa:0.2f}')
print(f'Salário do cliente: R${salario:0.2f}')
print(f'Valor da prestação: R$ {prestacao:0.2f}')
print(f'Valor máximo permitido para uma prestação: R${valormaximo:0.2f}')
print('*'*50)