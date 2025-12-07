"""
[Exercício 102]
    Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
def fatorial(num, show=False):
    """
    Docstring for fatorial

    fatorial(n, show=False)
    -> Calcula o fatorial de um número.
    
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.

    """
    total = 1
    print('=' * 100)
    if show == True:
        for cont in range (num, 0, -1):
            if cont > 1:
                print(cont, end = ' x ')
            if cont == 1:
                print(cont, end = ' = ')
            total *= cont
        return(total)
    if show == False:
        for cont in range (num, 0, -1):
            total *= cont
        return(total)
#Principal
print(fatorial(5, True))
print(fatorial(4, False))
print(fatorial(3))