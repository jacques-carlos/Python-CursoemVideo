"""
[Exercício 65]
    Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor dos valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
    
"""

continuar = 'S'
contador = 0
soma = 0
media = 0
maior = 0
menor = 0

print('')
print('='*130)
print('Esse programa irá ler números inteiros digitados pelo teclado e no final mostrará a média, o maior e o menor dos valores lidos.')

while continuar == 'S':
    print('')
    pergunta = str(input('Você deseja continuar?[S/N]: ')).upper().strip()
    
    if pergunta == 'S':
        continuar = 'S'
        numero = int(input('Digite seu número: \n'))
        soma += numero 
        if contador == 0:
            menor = numero
            maior = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
        contador += 1
    
    elif pergunta == 'N':
        continuar = 'N'
        print('Finalizando programa...')
    
    else:
        print('ERRO! Digite "S" para SIM e "N" para NÃO')
    
if contador != 0:
    media = soma/contador

print(f'''
Média: {media}
Menor valor: {menor}
Maior valor: {maior}
''')