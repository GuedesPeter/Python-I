'''Crie um algoritmo que leia um número e
mostre seu dobro,triplo e raiz quadrada.'''

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raizq = num ** (1/2)
print('O número {} tem como seu dobro {},\n seu triplo {}\n e sua raiz quadrada {}.'.format(num,dobro,triplo,raizq))