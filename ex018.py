'''Faça um programa que leia um ângulo qualquer
e mostre sa tela o valor do seno,cosseno e
tangente desse ângulo.'''



from math import sin,cos,tan,radians

angulo = float(input('Digite o ângulo desejado °: '))
print('O ângulo {} tem como seno {:.2f} - cosseno {:.2f} - tangente {:.2f}'.format(angulo,sin(radians(angulo)),cos(radians(angulo)),tan(radians(angulo))))


'''
A FUNÇÃO RADIANS É USADA PORQUE AOS PARAMETROS DAS 
FUNÇÕES SIN,COS,TAN SÃO PASSADOS EM RADIANOS,
ASSIM SENDO NECESSARIO A CONVERSÃO (ATRAVÉS DA FUNÇÃO RADIANS)
PARA CENTÍGRADOS.

import math
angulo = float(input('Digite o ângulo desejado °: '))
seno = math.sin(math.radians(angulo))
print('O SENO de {} é {:.2f}.'.format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print('O COSSENO de {} é {:.2f}.'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('A TANGENTE de {} é {:.2f}.'.format(angulo,tangente))
'''