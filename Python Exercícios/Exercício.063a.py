"""
[Exercício 63]
    Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
    
"""
print('Sequência de Fibonacci')
n = int(input('Quantos termos você deseja? '))
n1 = 0
n2 = 1
contador = 3
print(f'{n1} -> {n2} ->', end=' ')

while contador <= n:   
    n3 = n1 + n2
    print(n3, end=' -> ')
    contador += 1  
    n1 = n2
    n2 = n3   

print('Fim da Sequência de Fibonacci')