"""
**************************************************
AULA 17
**************************************************

        LISTAS
        variáveis compostas mutáveis
        pode haver dados diferentes nas listas (números e letras, por exemplo)
        del(lista) (apaga a lista)

"""


# CRIAÇÃO
num = [5, 7, 2, 3]
valores = list[5, 9, 4]
lista = list(range(4, 11))


print(f'RANGE: {lista}')
print(f'CRIAÇÃO: {num}')


# ADIÇÃO
num.append(4)
num.append(5)
num.insert(3, 8) # índice, elemento
num.insert(1, 7) # índice, elemento

print(f'ADIÇÃO: {num}')


# ALTERAÇÃO
num[2] = 5
num[7] = 9

print(f'ALTERAÇÃO: {num}')
             

# ORDENAMENTO
num.sort()
print(f'CRESCENTE: {num}')

num.sort(reverse=True)
print(f'DECRESCENTE: {num}')


# TAMANHO
print(f'Essa lista tem {len(num)} elementos')


# REMOÇÃO
del num[0] # índice
num.pop(1) # índice
num.pop 
num.remove(5) # elemento | remove apenas o primeiro elemento

print(f'REMOÇÃO: {num}')

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')


print('=-'*25)


# ENUMERATE
for p, v in enumerate(valores):
    print(f'Na posição {p} encontrei o número {v}')
print('Cheguei ao final da lista.')

# INPUT
for c in range (0,3):
    valores.append(int(input('Digite um valor: ')))
print(f'LISTA FINAL: {valores}')


print('=-'*25)


# LIGAÇÃO ENTRE LISTAS
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# CÓPIA ENTRE LISTAS
c = [2, 3, 4, 7]
d = a[:]
d[2] = 8
print(f'Lista C: {c}')
print(f'Lista D: {d}')