def aumentar(valor, porcentagem):
    return valor + (valor*porcentagem)/100


def diminuir(valor, porcentagem):
    return valor - (valor*porcentagem)/100 


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2

def moeda(valor):
    return f'R${valor:0.2f}'