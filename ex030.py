

'''Crie um programa que leia um número inteiro
 e mostre na tela se ele é PAR ou ÍMPAR.'''

from time import sleep
num = int(input('Digite um número qualquer: '))
print('PROCESSANDO... ... ...')
sleep(2)
if num %2 == 0:
    print('O número {} é PAR.'.format(num))
else:
    print('O número {} é ÍMPAR.'.format(num))

'''Se o resto da divisão (%) por 2 for igual a zero
o número será PAR,caso contrário será IMPAR.'''
