"""
[Exercício 49]
    Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.

    [Exercício 9] Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

"""

x=int(input('Informe um número inteiro qualquer para obter a sua tabuada:'))

print(f'Tabuada do número {x}:')
print('-'*20)
for y in range(1,11):
    print(f'{x:>5} x {y:>2} = {x*y:>2}')
print('-'*20)


'''  

    {x:20}       Solto
    {x:<20}      Esquerda
    {x:>20}      Direita
    {x:^20}      Centralizado
    {x:=^20}     Preenchido

'''