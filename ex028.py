

'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep #IMPORTA UM TIMER
computador = randint(0,5) #FAZ O COMPUTADOR PENSAR
print('=='*20)
print('Vou pensar em um número de 0 a 5.Tente adivinhar...')
print('=='*20)
jogador = int(input('Em que número pensei? ')) #JOGADOR TENTA ADIVINHAR
print('PROCESSANDO... ... ...')
sleep(2) #ADICIONA UM TIMER DE 2 SEG.
if jogador == computador:
    print('PARABÉNS!VOCÊ ACERTOU.')
else:
    print('QUE PENA,VOCÊ ERROU!Eu pensei no número {} e não em {}.'.format(computador,jogador))

