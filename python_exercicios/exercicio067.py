"""
[Exercício 67]
    Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
    
"""
print('')
print(f'{' Tabuada Matemática '.upper():~^60}')
print(f'{'Digite um NÚMERO NEGATIVO para ENCERRAR o programa':^60}')

while True:
    print('')
    valor = int(input('valor:'))
    if valor < 0:
        break
    print(f'{f' Tabuada do número {valor} '.upper():~^60}')
    for c in range(1,11):
        print(f'{valor:>25} x {c:>2} = {valor*c}')
    print('~'*60)
print('Volte sempre!')