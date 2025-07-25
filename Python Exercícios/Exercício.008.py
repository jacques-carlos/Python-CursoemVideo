"""
[Exercício 8]
    Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.
    Extra: converter também para quilômetros, hectômetros, decâmetros e decímetros.

"""

m=float(input('Digite seu valor em metros: '))

km=m/1000
hm=m/100
dam=m/10
dm=m*10
cm=m*100
mm=m*1000

print(f'Valor informado: {m}m')
print(f'Valor em quilômetros: {km}km')
print(f'Valor em hectômetros: {hm}hm')
print(f'Valor em decâmetros: {dam}dam')
print(f'Valor em decímetros: {dm}dm')
print(f'Valor em centímetros: {cm}cm')
print(f'Valor em milímetros: {mm}mm')