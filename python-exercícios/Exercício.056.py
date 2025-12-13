"""
[Exercício 56]
    Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:

    - A média de idade do grupo.
    - Qual é o nome do homem mais velho.
    - Quantas mulheres tem menos de 20 anos.

"""

media = 0               # Média de idade
idadevelho = 0          # Idade do homem mais velho
nomevelho = ''          # Nome do homem mais velho
c = 0                   # Contador
x = 0

for l in range(1,5):
    nome = str(input('Informe seu NOME: ')).title().strip()
    idade = int(input('Informe sua IDADE: '))
    sexo = str(input(f'Informe [H] para HOMEM e [M] para MULHER: ')).upper().strip()

    media += idade

    if sexo == 'H' and idade == idadevelho:
        nomevelho += ' e ' + nome
    elif sexo == 'H' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome

    if sexo == 'M' and idade < 20:
        c += 1
    if sexo == 'H':
        x += 1

print(f'A média de idade do grupo é de: {media/4:0.1f} anos')
if x == 0:
    print('Não há homens')
else:
    print(f'O homem mais velho é {nomevelho} com {idadevelho} anos')
print(f'Há {c} mulheres com menos de 20 anos')