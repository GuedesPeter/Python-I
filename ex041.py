'''

A Confederação Nacional de Natação
precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua ategoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
 Acima de 25 anos: MASTER
'''

#OBTENDO A DATA ATUAL PELA IMPORTAÇÃO DO MÓDULO.
from datetime import date
atual = date.today().year
#===============================================

nasc = int(input('Ano de nascimento do atleta: '))
idade = atual - nasc

if idade <= 9:
    print('Você tem {} anos.'.format(idade))
    print('Sua categoria é MIRIM.')
elif idade > 10 and idade <= 14:
    print('Você tem {} anos.'.format(idade))
    print('Sua categoria é INFANTIL.')
elif idade >= 15 and idade <= 19:
    print('Você tem {} anos.'.format(idade))
    print('Sua categoria é JÚNIOR.')
elif idade > 20 and idade <= 25:
    print('Você tem {} anos.'.format(idade))
    print('Sua categoria é SÊNIOR.')
else:
    print('Você tem {} anos.'.format(idade))
    print('Sua categoria é MASTER.')

