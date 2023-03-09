'''Faça um programa que leia um número inteiro
e mostre seu secessor e seu antecessor'''

num = int(input('Digite um número: '))
s = num + 1
a = num - 1
print('O número {},tem como sucessor {} e antecessor {}.'.format(num,s,a))