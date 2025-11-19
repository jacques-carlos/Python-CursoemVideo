"""
[Exercício 72]
    Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

    A) Apenas os 5 primeiros colocados.
    B) Os últimos 4 colocados da tebela.
    C) Uma lista com os times em ordem alfabética.
    D) Em que posição na tabela está o time da Chapecoense.
    
"""

tabela = ('Atlético-MG', 'Flamengo', 'Corinthians', 'Palmeiras', 'Fluminense', 'América-MG', 'São Paulo', 'Grêmio', 'Vasco',
          'Internacional', 'Botafogo', 'Sport', 'Cruzeiro', 'Vitória', 'Santos', 'Chapecoense', 'Athletico-PR', 'Bahia', 'Ceará', 'Paraná')

print('CAMPEONATO BRASILEIRO DE FUTEBOL')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Os 5 primeiros colocados são : {tabela[0:5]}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Os 4 últimos colocados são: {tabela[16:]}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Os clubes em ordem alfabética são: {sorted(tabela)}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'A Chapecoense está na {tabela.index('Chapecoense')+1}ª colocação')