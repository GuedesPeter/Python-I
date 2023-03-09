
'''
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’,
o programa se encerrará. Importante: use cores.

'''
from time import sleep
c=('\033[m', # sem cor
   '\033[0;30;41m', #vermelho
   '\033[0;30;42m', #verde
   '\033[0;30;43m', #amarelo
   '\033[0;30;44m', #azul
   '\033[0;30;45m', #roxo
   '\033[7;30m'  #branco
   );


def ajuda(com):
    titulo(f'Acessando o manualdo comando \'{com}\'', 4)
    print(c[6],end='')
    help(com)
    print(c[0],end='')
    sleep(2)

def titulo(msg,cor=0):
    tam = len(msg)
    print(c[cor],end='')
    print('-'*tam)
    print(msg)
    print('-'*tam)
    print(c[0],end='')
    sleep(1)

#PROGRAMA PRINCIPAL
comando = ''
while True:
    print('SISTEMA DE AJUDA PyHELP',2)
    comando = input('Função ou biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!',1)
