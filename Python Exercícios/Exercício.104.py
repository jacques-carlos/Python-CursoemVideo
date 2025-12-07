"""
[Exercício 104]
    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Pyhton,
só que fazendo a validação para aceitar apenas um valor numérico.

Ex:
    n = leiaInt('Digite um número')
"""
def leiaInt(text):
    while True: 
        valor = (input(text))
        if valor.isnumeric() == True:
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return valor

# Programa principal
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}.')