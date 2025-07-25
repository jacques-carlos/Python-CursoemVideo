"""
[Exercício 6]
    Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

"""

x=int(input('Digite um número: '))

print(f'O número escolhido foi {x}. O seu dobro é {x*2}, o seu triplo é {x*3} e a sua raiz quadrada é {pow(x,1/2):0.2f}.')