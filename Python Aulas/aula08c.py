"""
**************************************************
AULA 8 parte C
**************************************************

        emoji                           módulo para emojis
        emojize                         função que imprime emojis no código
        :globe_showing_Americas:        código de um emoji
"""

import emoji

print(emoji.emojize('Olá, Mundo! :globe_showing_Americas:'))

print(emoji.emojize('Olá, Mundo! :globe_showing_Americas:', language='alias')) #outra forma de fazer
