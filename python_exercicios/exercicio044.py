"""
[Exercício 44]
    Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

    - À vista dinheiro/cheque: 10% de desconto
    - À vista no cartão: 5% de desconto
    - Em até 2x no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros

"""

print('')
print(f'{' LOJAS GUANABARA ':=^150}')

valor = float(input('Valor do produto: R$'))

print('FORMAS DE PAGAMENTO\n[1] À vista no dinheiro/cheque (10% off)\n[2] À vista no cartão (5% off)\n[3] Em até 2x no cartão\n[4] 3x ou mais no cartão (20% de juros)')

pagamento = int(input('Forma de pagamento: '))
print('='*150)

if pagamento == 1:
    final = valor - 0.1*valor
    print(f'Valor do produto: R${valor:0.2f}')
    print('Pagamento: À vista')
    print('10% de desconto')
    print(f'Valor final: R${final:0.2f} ')

elif pagamento == 2:
    final = valor - 0.05*valor
    print(f'Valor do produto: R${valor:0.2f}')
    print('Pagamento: 1x no cartão')
    print('5% de desconto')
    print(f'Valor final: R${final:0.2f} em 1x')

elif pagamento == 3:
    final = valor / 2
    print(f'Valor do produto: R${valor:0.2f}')
    print('Pagamento: 2x no cartão')
    print(f'Valor final: 2x de R${final:0.2f}')
    print(f'Total: R${valor:0.2f}')

elif pagamento == 4:
    parcelas = int(input('Informe quantas parcelas(de 3x até 12x): '))
    if parcelas > 12 or parcelas == 0:
        print('Número de parcelas inválido (dividimos em até 12x), por favor tente novamente ')
    elif parcelas == 1 or parcelas == 2:
        print('Número de parcelas inválido, por favor reinicie o processo e preste mais atenção no menu de formas de pagamento')
    else:
        final = (valor + 0.2*valor) / parcelas
        total = valor + 0.2*valor
        print(f'Valor do produto: R${valor:0.2f}')
        print(f'Pagamento: {parcelas}x no cartão')
        print('20% de juros')
        print(f'Valor final: {parcelas}x de R${final:0.2f}')
        print(f'Total: R${total:0.2f}')

else:
    print('Opção inválida, tente novamente.')

print('='*150)
print('Obrigado pela preferência, volte sempre!')