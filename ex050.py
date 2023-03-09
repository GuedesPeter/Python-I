


'''
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.


'''

soma = 0
for pares in range(1,7):
    n = int(input('DIGITE UM NÚMERO: '))
    if n % 2 == 0:
        soma = soma + n
print('--'*40)
print('\033[7;31mA soma dos números PARES entre os seis digitados é {}.'.format(soma))

