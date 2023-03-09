

'''
Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de
uma Sequência de Fibonacci.
Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8

'''

print('--'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('--'*30)

n = int(input('Quantos termos você quer mostrar?  '))
termo1 = 0
termo2 = 1
print('{} >> {}'.format(termo1,termo2),end='')
contador = 3
while contador <= n:
    termo3 = termo1 + termo2
    print('>> {} '.format(termo3),end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print('>> FIM.')
