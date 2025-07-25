"""
**************************************************
AULA 12 parte A
**************************************************

            CONDIÇÕES ANINHADAS
            IF
            ELIFE
            ELSE

"""

nome = str(input('Qual é o seu nome? ')).title()

if nome == 'Gustavo':
    print('Que nome feio!')

elif nome == 'Maria' or nome == 'José' or nome == 'João':
    print('O seu nome é tão sem graça!')

else:
    print('O seu nome é normal!')

print(f'Tenha um bom dia, {nome}!')
