"""
[Exercício 98]
    Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.

    Seu programa tem que realizar três contagens através da função criada:

    a) De 1 até 10, de 1 em 1.
    b) De 10 até 0, de 2 em 2.
    c) Uma contagem personalizada.
"""
def contador(início, fim, passo):
    print('='*100)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}:')
    cont = início
    if cont < fim :
        while cont < fim: 
            print(cont, end=' ')
            cont += passo
    elif cont > fim:
        while cont > fim:
            print(cont, end = ' ')
            cont -= passo
    print('FIM!')
    print('='*100)

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora sua vez de personalizar uma contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))