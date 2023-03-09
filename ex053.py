


'''
Crie um programa que leia uma frase qualquer e
diga se ela é um palíndromo,
desconsiderando os espaços.

Exemplos de palíndromos:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
'''

print('''
Exemplos de palíndromos:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
''')


frase = str(input('Digite um PALÍNDROMO: ')).strip().upper()#ELIMINEI OS ESPAÇOS ATES DE DEPOIS
palavra = frase.split() #ELIMINEI OS ESPÇOS INTERNOS
junto = ''.join(palavra) #ELIMINEI OS ESPÇOS INTERNOS
inverso = ''

'''Vai começar em LEN(JUNTO) titando uma letra pois o tamanho vai de 0 a 19
Vai até a letra -1 que é antes da primeira
E vai voltando uma letra com -1'''
for letra in range(len(junto)-1,-1,-1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}.'.format(junto,inverso))
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('A FRASE DIGITADA NÃO É UM PALÍNDROMO.')



'''EXEMPLO SEM O FOR:

frase = str(input('Digite um PALÍNDROMO: ')).strip().upper()#ELIMINEI OS ESPAÇOS ATES DE DEPOIS
palavra = frase.split() #ELIMINEI OS ESPÇOS INTERNOS
junto = ''.join(palavra) #ELIMINEI OS ESPÇOS INTERNOS
inverso = junto[::-1]

print('O inverso de {} é {}.'.format(junto,inverso))
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('A FRASE DIGITADA NÃO É UM PALÍNDROMO.')
    
'''

