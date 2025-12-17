from utilidadescev import moeda

def leiaDinheiro(text):
    while True:
        valor = str(input(text)).strip().replace(',', '.')  
        if valor.isnumeric():
            return float(valor)   
        else:
            if valor.count('.') == 1:
                valor = float(valor)
                return valor
            else:
                print(f'\033[31mERRO: "{valor}" é um valor inválido!\033[m')