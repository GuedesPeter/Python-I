

'''CONDIÇÕES IF - ELIF - ELSE'''

'''
CONDIÇÃO SIMPLES: SOMENTE USANDO IF
CONDIÇÃO COMPOSTA: USAMOS IF , ELSE

EX.:
(SE)
IF CARRO.ESQUERDA():
    bloco TRUE

(SENÃO)    
ELSE:
    bloco FALSE
    
'''
#EX.:

tempo = int(input('Quanto tempo tem seu carro? '))
if tempo <= 3:
    print('CARRO NOVO!')
else:
    print('CARRO VELHO')
    print('FIM!!!!!!!!!')

'''
>>>>CONDIÇÃO SIMPLIFICADA<<<<

tempo = int(input('Quanto tempo tem seu carro? '))
print('carro novo'if tempo<=3 else'carro velho')
print('FIM!!!!!!!!!')

'''

#EX2.:
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
print('Sua média foi {}.'.format(media))
if media >= 6:
    print('Sua média foi boa.PARABÈNS!!!')
else:
    print('Você ficou abaixo da média.Estude Mais!')

