

'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

veloc = int(input('Digite a velocidade atual do carro Km/h: '))
if veloc > 80:
    print('Você excedeu o limite de velocidade!Será multado em R$7,00 por KM excedente.')
    multa = (veloc -80)* 7
    print('Você deve pagar R${:.2f} de multa.Tenha mais cuidado!'.format(multa))
else:
    print('Você está dentro da velocidade permitida.')
    print('Tenha um bom dia! Dirija com Segurança.')

