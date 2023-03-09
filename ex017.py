'''Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.'''

from math import hypot
cop = float(input('Cateto Oposto: '))
cad = float(input('Cateto Adjacente: '))

print('Cateto Oposto vale {} - Cateto Adjacente vale {} - Hipotenusa é {:.2f}.'.format(cop,cad,hypot(cop,cad)))

'''RESOLUÇÃO MATEMÁTICA SEM A BIBLIOTECA
cop = float(input('Cateto Oposto: '))
cad = float(input('Cateto Adjacente: '))
hipo = (cop**2 + cad**2) ** 1/2
print('A Hipotenusa mede {}.'.format(hipo))
'''