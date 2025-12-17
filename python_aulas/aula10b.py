"""
**************************************************
AULA 10 parte B
**************************************************

        CONDIÇÕES - NOMES
        ==      igual
        !=      diferente
        >       maior que
        <       menor que
        >=      maior ou igual
        <=      menor ou igual
"""

nome=str(input('qual é o seu nome? ')).title()

if nome == 'Gustavo':
    print('Que nome feio você tem!')
else:
    print('Que nome bonito você tem!')
print(f'bom dia, {nome}!')
