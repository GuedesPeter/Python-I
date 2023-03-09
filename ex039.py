'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade:
se ele ainda vai se alistar ao serviço militar;
se é a hora exata de se alistar
se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

'''

#OBTENDO A DATA ATUAL PELA IMPORTAÇÃO DO MÓDULO.
from datetime import date
atual = date.today().year
#===============================================

nasc = int(input("Ano de nascimento: "))
idade =  atual - nasc
print('Quem nasceu em {} e tem {} anos de idade.'.format(nasc,idade))

if idade == 18:
    print('Aliste-se Imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Voce não tem idade. Ainda faltam {} anos para o alistamento.'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Voce deveria ter se alistado a {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento deveria ter sido em {}.'.format(ano))
