"""
**************************************************
AULA 21 parte b
**************************************************
        FATORIAL DE UM NÚMERO
"""


def fatorial(num=1):
    total = 1
    while True:
        total *= num
        num -= 1
        if num <= 1:
            break
    return (total)


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
