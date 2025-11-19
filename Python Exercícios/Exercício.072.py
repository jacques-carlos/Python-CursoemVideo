"""
[Exercício 72]
    Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
    
"""

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

escolha = int(input('Digite um número entre 0 e 20: '))

while escolha > len(extenso):
    escolha = int(input('Número inválido. Digite um número entre 0 e 20:'))

print(f'Você digitou o número {extenso[escolha]}')
