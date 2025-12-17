"""
[Exercício 75]
    Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.
    
"""

print('')
print('=-'*50)
print('')


tupla = (int(input('[1/4] Digite um número: ')),
        int(input('[2/4] Digite um número: ')),
        int(input('[3/4] Digite um número: ')),
        int(input('[4/4] Digite um número: ')))

print('')
print('=-'*50)
print('')

print('Você digitou os números:', tupla)
   
print(f'O número 9 apareceu {tupla.count(9)} vezes')

if tupla.count(3) > 0:  #if 3 in tupla:
    print(f'O primeiro número 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O número 3 não apareceu')

print('Os números pares são:', end=' ')
    
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')