"""
[Exercício 76]
    Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
    Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

"""

palavra = ''
c = 0
tupla = ('casa', 'bolacha', 'rato', 'joaninha', 'mercado', 'tatu', 'abacate')

for palavra in tupla:
    print('')
    print(f'Na palavra {palavra.upper()} temos as vogais: ', end='')

    for c in range(0, len(palavra)):

        if palavra[c] == 'a':
            print('a', end=' ')

        elif palavra[c] == 'e':
            print('e', end=' ')

        elif palavra[c] == 'i':
            print('i', end=' ')

        elif palavra[c] == 'o':
            print('o', end=' ')

        elif palavra[c] == 'u':
            print('u', end=' ')

        c += 1
