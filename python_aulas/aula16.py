"""
**************************************************
AULA 16
**************************************************

        TUPLAS
        variáveis compostas imutáveis
        pode haver dados diferentes nas tuplas (números e letras, por exemplo)
        del(tupla) (apaga a tupla)

"""

lanche = ('Hambúrguer', 'Bolo', 'Pizza', 'Pudim', 'Lasanha', 'Sorvete')

print(lanche)
print(sorted(lanche))

print('MANEIRA 1')
for comida in lanche:
    print(comida)

print('MANEIRA 2')
for c in range (0, len(lanche)):
    print(lanche[c])

print('MANEIRA 3')
for pos, comida in enumerate(lanche):
  print(f'{pos}: {comida}')


bebida = ('Suco', 'Água', 'Sorvete', 'Refrigerante', 'Café')


tudo = bebida + lanche # ou tudo = lanche + medida
print(tudo)
print (tudo.count('Sorvete'))
print(tudo.index('Sorvete'))
print(tudo.index('Sorvete', 5))