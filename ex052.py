

'''
Faça um programa
que leia um número inteiro e diga se ele é ou não um número primo.

'''

print('\033[30mDESCOBRINDO NÚMEROS PRIMOS: ')
print('--'*30)

num = int(input('Escolha um número: '))
total = 0

for contador in range(1,num + 1):
    if num % contador == 0:
        print('\033[33m',end=' ')
        total = total + 1
    else:
        print('\033[31m',end=' ')
    print('{} '.format(contador),end='')

print('>>> O número {} foi divisível {} vezes.'.format(num,total))
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
