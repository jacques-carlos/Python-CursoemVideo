"""
[Exercício 83]
    Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
    Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
    
"""

expre = 'correta'
x = 0
lista = str(input('Digite sua expressão numérica: '))

lista.split()

a = lista.count('(')
b = lista.count(')')
if a != b:
    expre = 'incorreta'

while True:
    for i in range (0, len(lista)):
        if lista[i] == '(':
            x += 1
        if lista[i] == ')':
            x -= 1
        if x < 0:
            expre = 'incorreta'
            break
    break    

if expre == 'correta':        
    print('Essa expressão numérica está correta!')
elif expre == 'incorreta':
    print('Essa expressão numérica está incorreta!')
    

