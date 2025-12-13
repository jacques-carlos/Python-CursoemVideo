"""
[Exercício 37]
    Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

   - 1 para binário
   - 2 para octal
   - 3 para hexadecimal

"""

print('*'*100)


numero = int(input('Digite seu número inteiro: '))

print('Agora verifique em qual base seu número será convertido: ')
print('- (1) para converter em binário\n- (2) para converter em octal\n- (3) para converter em hexadecimal')

x = int(input('Dentre as opções a base desejada é: '))

print('...')

if x == 1:
    #print(f'Seu número em binário é: {bin(numero)[2:]}')
    print(f'Seu número em binário é: {numero:b}')
elif x == 2:
    #print(f'Seu número em octal é: {oct(numero)[2:]}')
    print(f'Seu número em octal é: {numero:o}')
elif x == 3:
    #print(f'Seu número em hexadecimal é: {hex(numero)[2:]}')
    print(f'Seu número em hexadecimal é: {numero:x}')
else:
    print('ERRO! Por favor, reinicie o programa e selecione um número válido.')


print('*'*100)