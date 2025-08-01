"""
[Exercício 63]
    Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
    
"""

print('Sequência de Fibonacci')
n = int(input('Digite um número inteiro: '))
n1 = n
n2 = n
n3 = n1 + n2
contador = 0

while contador < n:
    
    if contador < n:
        contador += 1
        print(n1, end=' -> ')
    
    if contador < n:
        contador += 1
        print(n2, end=' -> ')
    
    if contador < n:
        contador += 1
        print(n3, end=' -> ')
       
    n1 = n2 + n3
    n2 = n1 + n3
    n3 = n1 + n2
    
print('Fim da Sequência de Fibonacci')