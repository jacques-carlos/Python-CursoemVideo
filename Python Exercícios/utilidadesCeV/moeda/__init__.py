def linha(q):
    print('=' * q)


def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def aumentar(valor, porcentagem, format=False):
    resultado = valor + (valor*porcentagem)/100
    if format:
        return f'R${resultado:.2f}'
    else:
        return resultado

def diminuir(valor, porcentagem, format=False):
    resultado = valor - (valor*porcentagem)/100
    if format:
        return f'R${resultado:.2f}'
    else:
        return resultado


def dobro(valor, format=False):
    resultado = valor * 2
    if format:
        return f'R${resultado:.2f}'
    else:    
        return valor * 2


def metade(valor, format=False):
    resultado = valor / 2
    if format:
        return f'R${resultado:.2f}'    
    else:    
        return valor / 2


def resumo(valor, a, d):
    linha(30)
    print(f'{'RESUMO DO VALOR':^30}')
    linha(30)
    print(f'{'Preço analisado:':<20}{moeda(valor):>10}')
    print(f'{'Dobro do preço:':<20}{dobro(valor, True):>10}')
    print(f'{'Metade do preço:':<20}{metade(valor, True):>10}')
    print(f'{f'{a}% de aumento:':<20}{aumentar(valor, a, True):>10}')
    print(f'{f'{d}% de redução:':<20}{diminuir(valor, d, True):>10}')
    linha(30)