'''Escreva um programa que converta a temperatura
digitando em graus Célcius para Fahrenheit.'''

c = float(input('Temperatura °C: '))
f = ((9 * c)/5)+32
print('A temperatura de {}°C equivale a {}°F.'.format(c,f))
