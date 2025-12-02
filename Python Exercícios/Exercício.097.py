"""
[Exercício 97]
    Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

    Ex:
            escreva('Olá, Mundo!')
    Saída:
            ===========
            Olá, Mundo!
            ===========
"""
def escreva(texto):
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'{texto:^{tamanho}}')
    print('~' * tamanho)

escreva('Testando... 1... 2... 3...')
escreva('Olá, Mundo!')
escreva(str(input('Digite seu texto: ')))