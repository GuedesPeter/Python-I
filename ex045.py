

'''
Crie um programa que faça o computador jogar Jokenpô com você.

'''

from random import randint
from time import sleep
print('''\033[2;32m
JOKENPÔ :
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA
''')
escolha = int(input('\033[2;32mEscolha uma opção: '))
sleep(1)
print('\033[7;32mJO')
sleep(1)
print('\033[7;32mKEN')
sleep(1)
print('\033[7;32mPÔ!')
sleep(2)
print('\033[7;32m... ... ...')
pc = randint(1,3)

if pc == 1 and escolha == 3:
    print('\033[2;32mCOMPUTADOR ESCOLHEU {} E VOCÊ {} .PEDRA! VOCÊ PERDEU.'.format(pc,escolha))
elif pc == 2 and escolha == 1:
    print('\033[2;32mCOMPUTADOR ESCOLHEU {} E VOCÊ {} .PAPEL! VOCÊ PERDEU.'.format(pc,escolha))
elif pc == 3 and escolha == 2:
    print('\033[2;32mCOMPUTADOR ESCOLHEU {} E VOCÊ {} .TESOURA! VOCÊ PERDEU.'.format(pc,escolha))
elif pc == 1 and escolha == 2:
    print('\033[2;32mCOMPUTADOR ESCOLHEU {} E VOCÊ {} PAPEL! VOCÊ GANHOU.PARABÉNS!!!'.format(pc,escolha))
elif pc == 2 and escolha == 3:
    print('\033[2;32mCOMPUTADOR ESCOLHEU {} E VOCÊ {} .TESOURA! VOCÊ GANHOU.PARABÉNS!!!'.format(pc,escolha))
elif pc == 3 and escolha == 1:
    print('\033[2;32mCOMPUTADOR ESCOLHEU {} E VOCÊ {} .PEDRA! VOCÊ GANHOU.PARABÉNS!!!'.format(pc,escolha))
elif pc == escolha:
    print('\033[2;32mCOMPUTADOR ESCOLHEU {} E VOCÊ {} .EMPATE!! JOGUE NOVAMENTE.'.format(pc,escolha))
else:
    print('\033[2;32mOPÇÃO INVÁLIDA! PERMITIDO - PEDRA[1],PAPEL[2] E TESOURA[3].')
