


'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.

'''

from datetime import date

atual = date.today().year

maior = 0
menor = 0
for media in range(1,8):
    nasc = int(input('Digite o seu ano de nascimento: '))
    idade = atual - nasc
    if idade >= 21:
        print('Essa pessoa atingiu a maior idade.')
        maior += 1
    else:
        print('Essa pessoa não atingiu a maior idade.')
        menor += 1

print('Temos {} pessoas maiores de idade '.format(maior),end='')
print('e temos {} pessoas menores de idade!'.format(menor))
