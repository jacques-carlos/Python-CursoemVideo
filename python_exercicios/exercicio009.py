"""
[Exercício 9]
    Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

"""

x=int(input('Informe um número inteiro qualquer para obter a sua tabuada:'))

print(f'Tabuada do número {x}:')
print('-'*20)
print(f'{x:>6} x {1:>2} = {x*1:>2}')
print(f'{x:>6} x {2:>2} = {x*2:>2}')
print(f'{x:>6} x {3:>2} = {x*3:>2}')
print(f'{x:>6} x {4:>2} = {x*4:>2}')
print(f'{x:>6} x {5:>2} = {x*5:>2}')
print(f'{x:>6} x {6:>2} = {x*6:>2}')
print(f'{x:>6} x {7:>2} = {x*7:>2}')
print(f'{x:>6} x {8:>2} = {x*8:>2}')
print(f'{x:>6} x {9:>2} = {x*9:>2}')
print(f'{x:>6} x {10} = {x*10:>2}')
print('-'*20)

#   {:20}
#   {:<20}
#   {:>20}
#   {:^20}
#   {:=^20}