"""
[Exercício 67]
    Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
    
"""

titulo = ' TABUADA MATEMÁTICA '
info = 'Digite um NÚMERO NEGATIVO para ENCERRAR o programa'
print('')
print(f'{titulo:~^60}')
print(f'{info:^60}')

while True:
    print('')
    valor = int(input('valor:'))
    if valor < 0:
        break
    subtitulo = f' TABUADA DO NÚMERO {valor} '
    print(f'{subtitulo:~^60}')
    for c in range(1,11):
        print(f'{valor:>25} x {c:>2} = {valor*c}')
    print('~'*60)
print('Volte sempre!')