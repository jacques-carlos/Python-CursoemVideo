"""
[Exercício 65]
    Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor dos valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
    
"""
continuar = 'S'
contador = soma = media = maior = menor = 0 

print('')
print('='*130)
print('Esse programa irá ler números inteiros digitados pelo teclado e no final mostrará a média, o maior e o menor dos valores lidos.')

while continuar == 'S':
    numero = int(input('Digite seu número: \n'))
    contador += 1
    soma += numero 
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        
    pergunta = str(input('Você deseja continuar?[S/N]: ')).upper().strip()[0]
    if pergunta == 'N':
        continuar = 'N'
        print('Finalizando programa...')   
    elif pergunta == 'S':
        print('')
    else:
        print('ERRO! Digite "S" para SIM e "N" para NÃO')
        break
    
media = soma/contador

print(f'''
Média: {media}
Menor valor: {menor}
Maior valor: {maior}
''')