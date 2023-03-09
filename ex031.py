

'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.'''

from time import sleep
distancia = float(input('Qual a distância da viagem KM? '))
if distancia <= 200:
    preco = distancia*0.5
    print('CALCULANDO... ... ...')
    sleep(2)
    print('O custo da sua viagem será de R${:.2f}.'.format(preco))
else:
    preco = distancia * 0.45
    print('CALCULANDO... ... ...')
    sleep(2)
    print('O custo da sua viagem será de R${:.2f}.'.format(preco))
