def linha(q):
    print('=' * q)


def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def aumentar(valor, porcentagem, formato=False):
    resultado = valor + (valor*porcentagem)/100
    if formato:
        return moeda(resultado)
    else:
        return resultado


def diminuir(valor, porcentagem, formato=False):
    resultado = valor - (valor*porcentagem)/100
    if formato is True:
        return moeda(resultado)
    else:
        return resultado


def dobro(valor, formato=False):
    resultado = valor * 2
    if formato is False:
        return resultado
    else:    
        return moeda(resultado)


def metade(valor, formato=False):
    resultado = valor / 2
    if  not formato:
        return resultado
    else:    
        return moeda(resultado)        


def resumo(valor, a=10, d=5): # a:aumento d:dimunuição
    linha(30)
    print('RESUMO DO VALOR'.center(30))
    linha(30)
    print(f'{'Preço analisado:':<20}{moeda(valor):>10}')
    print(f'{'Dobro do preço:':<20}{dobro(valor, True):>10}')
    print(f'{'Metade do preço:':<20}{metade(valor, True):>10}')
    print(f'{f'{a}% de aumento:':<20}{aumentar(valor, a, True):>10}')
    print(f'{f'{d}% de redução:':<20}{diminuir(valor, d, True):>10}')
    linha(30)

# \t{metade(valor, True)} adicionaria uma tabulação