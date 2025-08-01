"""
[Exercício 59]
    Crie um programa que leia dois valores e mostre um menu na tela:
        [1] Soma
        [2] Multiplicador
        [3] Maior
        [4] Novos números
        [5] Sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso.

"""

from time import sleep as delay
menu = 0

while menu != 5:
    print('''
------------------MENU MATEMÁTICO------------------
Primeiramente, informe dois valores:
''')
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))    
    
    print('''
------------------MENU MATEMÁTICO------------------
Selecione uma das seguintes opções:
    [1] Soma
    [2] Multiplicador
    [3] Maior
    [4] Novos números
    [5] Sair do programa
''')
    
    menu = (int(input('Me infome o que você quer fazer: ')))
    if menu == 1:
        soma = n1 + n2
        print(f'Sua soma é: {soma}')
    elif menu == 2:
        multiplicação = n1 * n2
        print(f'Sua multiplicação é: {multiplicação}')
    elif menu == 3:
        maior = max(n1, n2)
        print(f'O maior número é: {maior}')
    elif menu == 4:
        print('Aguarde um instante...')
        delay(2)
    elif menu == 5:
        print('Encerrando o programa...')
        delay(3)
    else:
        print('ERRO!\nOpção inválida, tente novamente.')
        delay(2)

print('Volte sempre que precisar!')