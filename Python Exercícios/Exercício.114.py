"""
[Exercício 114]
    Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
"""
import requests
try:
    teste = requests.get('https://pudim.com.br/', timeout=10)
except:
    print('\033[31mO site Pudim não está acessível no momento.\33[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')