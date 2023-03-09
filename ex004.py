'''Faça um programa que leia algo pelo teclado e
mostre na tela seu tipo primitivo e todas as
informações possiveis sobre ele.'''

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('È somente espeços?',a.isspace())
print('È um número?',a.isalnum())
print('È alfanumérico?',a.isalpha())
print('Está em letras maiúsculas?',a.isupper())
print('Esta em letras minúsculas?',a.islower())