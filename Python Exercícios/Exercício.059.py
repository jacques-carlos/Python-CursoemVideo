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

print('''
==================== MENU MATEMÁTICO ====================
Primeiramente, informe dois valores:
''')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))    

while menu != 5: 
    print(f'''
==================== MENU MATEMÁTICO ====================
PRIMEIRO: {n1}
SEGUNDO: {n2}

Selecione uma das seguintes opções:
    [1] Soma
    [2] Multiplicador
    [3] Maior
    [4] Novos números
    [5] Sair do programa
''')
    
    menu = (int(input('Me infome o que você quer fazer >>>>>>>>> ')))
    
    if menu == 1:
        soma = n1 + n2
        print(f'O resultado de {n1} + {n2} é: {soma}')
        print('')
        print('Voltando ao Menu Inicial...')
        delay(2)
    
    elif menu == 2:
        multiplicação = n1 * n2
        print(f'O resultado de {n1} x {n2} é: {multiplicação}')
        print('')
        print('Voltando ao Menu Inicial...')
        delay(2)
    
    elif menu == 3:
        maior = max(n1, n2)
        print(f'O maior número entre {n1} e {n2} é: {maior}')
        print('')
        print('Voltando ao Menu Inicial...')
        delay(2)
    
    elif menu == 4:
        print('Aguarde um instante...')
        delay(2)
        print('''
==================== MENU MATEMÁTICO ====================
Informe dois valores:
''')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))    
    
    elif menu == 5:
        print('Encerrando o programa...')
        delay(3)
    
    else:
        print('ERRO!\nOpção inválida, tente novamente.')
        delay(2)

print('Volte sempre que precisar!')