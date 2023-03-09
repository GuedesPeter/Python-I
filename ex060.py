

'''
Faça um programa que leia um número qualquer
e mostre o seu fatorial.
Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120

'''

'''
from math import factorial
num = int(input('FATORIAL DE : '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num,f))

'''
num = int(input('FATORIAL DE : '))
contador = num
fatorial = 1 #inicia em 1 pois se multiplicar por zero ira gerar resultado 0
print('{}! = '.format(contador),end='')
while contador > 0:
    print('{}'.format(contador),end='')
    print(' x ' if contador > 1 else ' = ',end='')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))

'''--------------------------------------------------------------------'''



