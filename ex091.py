'''
Crie um programa onde
4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.

'''

from random import randint
from time import sleep
#modulo para organizar o dicionário
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)
}

#LISTA RANKING criada para ordenar a classificação do jogo
ranking = []

print('VALORES SORTEADOS:')
print('--'*30)
for k,v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)

print('--'*30)
#ordenando os resultados do ranking do 1° ao ultimo colocado
#ITEMGETTER[1] PARA ORDENAR POR VALOR - [0] ORDENA POR CHAVE(KEYS)
#Neste caso quero ordenar pelo valor - ITEMGETTER[1]
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
print('--'*30)
#RANKING ORDENADO E RETORNADO EM UMA LISTA POR ISSO O ENUMERATE
#PARA PRINTAR A CLASSIFICAÇÃO
for i,v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)





