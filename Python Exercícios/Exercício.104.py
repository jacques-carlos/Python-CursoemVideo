"""
[Exercício 104]
    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Pyhton,
só que fazendo a validação para aceitar apenas um valor numérico.

Ex:
    n = leiaInt('Digite um número')
"""
def leiaInt(text):
    while True: 
        valor = str(input(text))
        if valor.isnumeric() == True:
            return valor
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
# Programa principal
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}.')