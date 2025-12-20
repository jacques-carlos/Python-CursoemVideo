"""
**************************************************
AULA 10 parte A - if + else
**************************************************

        CONDIÇÕES - CARROS
        if simplificado:
        ex: print('carro novo' if tempo<=3 else 'caro velho')
"""

tempo = int(input('informe quantos anos tem o seu carro: '))

if tempo <= 3:
    print('seu carro está novo, mas não por muito tempo :)')

else:
    print('seu carro está velho, compre outro :)')

print('entre em contato: 4002-8922 e financie seu carro novo')
