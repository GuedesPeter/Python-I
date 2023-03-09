'''Escreva um programa que leia o valor em metro,
eo exiba em centímetros'''

metros = float(input('Digite a distância em Metros: '))
km = metros * 1000
hm = metros * 100
deca = metros * 10
deci = metros / 10
cm = metros/100
mm = metros / 1000
print('KM-{}\nHectometro-{}\nDecâmetro-{}\nMetro-{}\nDecímetro-{}\nCentímetro-{}\nMilímetro-{}'.format(km,hm,deca,metros,deci,cm,mm))