"""
**************************************************
AULA 13 parte A
**************************************************

        LAÇO DE VARIÁVEL DE CONTROLE
        ESTRUTURA DE REPETIÇÃO FOR

        for c in range(1,10):
            passo
        pega

"""

for x in range(0,5):
    print('OI!')
print('TCHAU!')

for x in range(0,6):
    print(x)
print('FIM!')

for x in range(5,-1,-1):
    print(x)
print('FIM!')

inicio = int(input('Digite o número INICIAL: '))
fim = int(input('Digite o número FINAL: '))
passo = int(input('Digite o PASSO: '))
for z in range(inicio, fim+1 , passo):
    print(z)
print('FIM!')

s = 0
for y in range (0,4):
    n = int(input('Digite um valor: '))
    s += n
print(f'Seu valor total é: {s}')