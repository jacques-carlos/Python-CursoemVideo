"""
[Exercício 113]
    Reescreva a função leiaInt() que fizemos no DESAFIO 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
    Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
def leiaInt(num):
    while True:
        try: 
            valor = int(input(num))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return valor


def leiaFloat(num):
    while True:
        try: 
            valor = float(input(num))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
        else:
            return valor
        

# Programa principal
i = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {i} e o valor real digitado foi {f}.')