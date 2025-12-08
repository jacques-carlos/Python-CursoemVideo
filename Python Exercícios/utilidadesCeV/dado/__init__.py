from utilidadesCeV import moeda

def leiaDinheiro(text):
    valor = str(input(text))
    valor = valor.replace(',', '.')  
    if valor.isnumeric():
        valor = float(valor)
        return moeda.resumo(valor, 80, 35)
    else:
        if valor.count('.') == 1:
            valor = float(valor)
            return moeda.resumo(valor, 80, 35)
        else:
            print(f'\033[31mERRO: "{valor}" é um valor inválido!\033[m')