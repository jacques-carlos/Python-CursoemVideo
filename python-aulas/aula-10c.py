"""
**************************************************
AULA 10 parte C
**************************************************

        CONDIÇÕES - NOTAS
        if                  condições simples
        if + else           condições compostas
        indentação (tabulação)
"""

print('*'*50)

nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))
media = (nota1 + nota2) /2

print(f'sua média é {media:.1f}')

if media<6:
    print('reprovado! que pena, estude mais!')
else:
    print('aprovado! não fez mais que a obrigação!')

print('*'*50)