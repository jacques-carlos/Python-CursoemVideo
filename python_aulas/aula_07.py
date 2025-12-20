"""
**************************************************
AULA 7 - tipos primitivos; operadores matemáticos
**************************************************

            (input)                     recebe dados do usuário
            TIPOS PRIMITIVOS:
            int(input)                  especifica números inteiros
            float(input)                especifica números reais
            str(input)                  especifica strings
            bool                        especifica números lógicos (True/False)
"""

n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))

s = n1+n2  # soma
m = n1*n2  # multiplicação
d = n1/n2  # divisão
i = n1//n2  # divisão inteira
e = n1**n2  # exponenciação

print(f'sua soma é {s} \nsua multiplicação é {m}')
print(f'sua divisão é {d:.2f}')
print(f'sua divisão inteira é {i}', end=' ')
print(f'e sua exponenciação é {e}')

"""
    f           f-strings (permite encaixar variáveis dentro das strings)
    /n          quebra de linha    
    :.2f        especificar casas decimais (nesse caso, duas)
    end=' '     junção de linha (nesse caso, adiciona um espaço em branco
"""
