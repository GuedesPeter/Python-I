'''Crie um programa que leia um número real
qualquer pelo teclado e mostre sua porção inteira.'''


'''IMPORTANDO UMA FUNCIONALIDADE DA BIBLIOTECA
from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num,trunc(num)))

IMPORTANDO A BIBLIOTECA TODA
import math
num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num,math.trunc(num)))
'''

'''USANDO A FUNÇÃO INT - SEM IMPORTAR A BIBLIOTECA MATH'''
num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num,int(num)))