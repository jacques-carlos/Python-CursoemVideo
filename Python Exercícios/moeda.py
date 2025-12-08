def aumentar(valor, porcentagem, format=False):
    resultado = valor + (valor*porcentagem)/100
    if format:
        return f'R${resultado:0.2f}'
    else:
        return resultado

def diminuir(valor, porcentagem, format=False):
    resultado = valor - (valor*porcentagem)/100
    if format:
        return f'R${resultado:0.2f}'
    else:
        return resultado


def dobro(valor, format=False):
    if format:
        return f'R${valor * 2:0.2f}'
    else:    
        return valor * 2


def metade(valor, format=False):
    if format:
        return f'R${valor / 2:0.2f}'
    else:    
        return valor / 2


def moeda(valor):
    return f'R${valor:0.2f}'