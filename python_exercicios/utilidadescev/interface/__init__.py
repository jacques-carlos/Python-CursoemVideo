def linha(simb, tam):
    return (simb*tam)


def título(text):
    print(f'\33[36m{linha('=',50)}\33[m')
    print(f'\033[1;34m{text.upper().center(50)}\033[m')
    print(f'\33[36m{linha('=',50)}\33[m')


def menu(lista):
    título('Menu principal')
    print(linha('~', 50))
    for i, v  in enumerate(lista):
        print(f'\033[1;34m{i+1} -\033[m {v}')
    print(linha('~', 50))
    option = leiaInt('\033[1;34mSua opção: \033[m')
    return option


def leiaInt(pergunta):
    while True:
        try: 
            valor = int(input(pergunta))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return valor
        

def leiaStr(pergunta):
    while True:
        try:
            nome = str(input(pergunta))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse nome.\033[m')
            return 'Desconhecido'
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um nome válido.\033[m')
        else:
            return nome