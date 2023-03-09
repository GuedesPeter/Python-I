

'''
Melhore o jogo do DESAFIO 28 onde o computador
vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''
'''
#MINHA RESOLUÇÃO

from time import sleep
from random import randint
contador = 0

while True:
    escolha = int(input('Escolha um número entre 0 e 10: '))
    sleep(1),print('Você escolheu o número {}.'.format(escolha))
    pc = randint(0, 10)
    sleep(0.5),print('O Computador escolheu o número {}.'.format(pc))
    contador +=1
    if escolha == pc:
        print('PARABÉNS,VOCÊ ACERTOU!!')
        print('Você precisou de {} tentativas para acertar!'.format(contador))

    else:
        escolha = int(input('VOCÊ ERROU! Escolha um número entre 0 e 10: '))
'''

#RESOLUÇÃO CURSO EM VÍDEO

from random import randint
computador = randint(0,10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar?')
acertou = False
palpites = 0

#ENQUANTO VOCÊ NÃO ACERTAR
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais!... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos!... Tente mais uma vez.')
print('Acertou com {} tentativas! PARABÉNS.'.format(palpites))



