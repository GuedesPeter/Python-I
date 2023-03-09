'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato de Basquete [NBA]
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da BULLS.

'''

nba = ("HEAT","CELTICS","BUCKS","76ERS","RAPTORS","BULLS",
       "NETS","HAWKS","CAVALIERS","HORNETS","SUNS",
       "GRIZZLIES","WARRIORS","MAVERICKS","JAZZ","NUGGETS",
       "TIMBERWOLVES","PELICANS","CLIPPERS","SPURS")
cont = 0
for pos,time in enumerate(nba):
    cont += 1
    print(f'{cont}° - {time}')
print('--'*40)
print(f'A) Os 5 primeiros colocados são: {nba[:5]}')
print('--'*40)
print(f'B) Os 4 ultimos colocados são: {nba[-4:]}')
print('--'*40)
print(f'C) Seguem os times em ordem:{sorted(nba)}')
print('--'*40)
print(f'D) O CHICAGO BULLS está em {nba.index("BULLS")+1}° colocado.')

