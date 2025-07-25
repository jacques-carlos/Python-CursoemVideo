"""
**************************************************
AULA 9 parte A
**************************************************

             CADEIA DE STRINGS:
             fatiamento
             análise
             divisão
"""

# [FATIAMENTO]

frase = 'Olá Mundo'

print('-'*20)
print('FATIAMENTO:')

print(frase[4:])        # caractere 4 até final
print(frase[:3])        # início até o caractere 3
print(frase[0:7])       # caractere 0 ao 7
print(frase[1:7:2])     # caractere 1 ao 7 andando dois em dois
print(frase[::2])       # inicío até final andando dois em dois
print(frase[1::3])      # caractere 1 até final andando três em três


# [ANÁLISE]

exemplo = '  Olá Planeta '

print('-'*20)
print('ANÁLISE:')

#len
print(len(exemplo))
#comprimento em caracteres da string

#count
print(exemplo.count('a'))
#conta a quantidade de caracteres na string (do caractere especificado)

#find
print(exemplo.find('l',0,9))
#mostra a(s) localização(s) do(s) caractere(s) especificado(s)

#in
print('Planeta' in exemplo)
#verifica se dentro da string existe o que foi pedido

#replace
print(exemplo.replace('Planeta', 'Mundo'))
#troca strings

#upper()
print(exemplo.upper())
#maiúsculas

#lower()
print(exemplo.lower())
#minúsculas

#capitalize
print(exemplo.capitalize())
#apenas o primeiro caractere em maiúsculo

#title
print(exemplo.title())
#o primeiro caractere de cada palavra será maiúsculo

#strip
print(exemplo.strip())  #ambas
print(exemplo.rstrip()) #direita
print(exemplo.lstrip()) #esquerda
#limpa os espaços excedentes


# [DIVISÃO]

string = 'Olá Sistema Solar'

print('-'*20)
print('DIVISÃO:')

#split()
print(string.split())
#separa palavras

#join
print('-'.join(string))
#juntar palavras com o caractere determinado (nesse caso, "-")
