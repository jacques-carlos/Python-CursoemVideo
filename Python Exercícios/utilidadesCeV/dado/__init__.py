from utilidadesCeV import moeda

def leiaDinheiro(text):
    valor = str(input(text))
    valor = valor.replace(',', '.')  
    if valor.isnumeric():
        valor = float(valor)
        return valor
    else:
        if valor.count('.') == 1:
            valor = float(valor)
            return valor
        else:
            print(f'\033[31mERRO: "{valor}" é um valor inválido!\033[m')