"""
[Exercício 98]
    Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.

    Seu programa tem que realizar três contagens através da função criada:

    a) De 1 até 10, de 1 em 1.
    b) De 10 até 0, de 2 em 2.
    c) Uma contagem personalizada.
"""
from time import sleep
def contador(início, fim, passo):
    # definindo contagem como crescente/decrescente
    if início < fim:
        contagem = 'crescente'
    elif início > fim:
        contagem = 'decrescente'
    else:
        contagem = 'erro'
    # caso o passo seja definido como zero
    if passo == 0:
        if contagem == 'crescente':
            passo = 1
        elif contagem == 'decrescente':
            passo = -1
    # contagem crescente não pode ter passo negativo, o contrário pode
    if passo < 1 and contagem == 'crescente':
        contagem = 'erro'
    # PRINTANDO CONTAGEM
    if contagem == 'erro':
        print('ERRO!')
    else:               
        # título
        print('='*100)
        if passo > 0:
            print(f'Contagem de {início} até {fim} de {passo} em {passo}:')
        if passo < 0:
            módulo = -passo
            print(f'Contagem de {início} até {fim} de {módulo} em {módulo}:')
        # crescente
        if contagem == 'crescente' :
            for c in range(início, fim+1, passo):
                print(c, end = ' ', flush=True)
                sleep(0.5)
        # decrescente
        elif contagem == 'decrescente':
            if passo > 0:
                passo = -passo
                for c in range(início, fim-1, passo):
                    print(c, end = ' ', flush=True)
                    sleep(0.5)
            elif passo < 0:
                for c in range(início, fim-1, passo):
                    print(c, end = ' ', flush=True)
                    sleep(0.5)
        print('FIM!')
        print('='*100)

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora sua vez de personalizar uma contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))